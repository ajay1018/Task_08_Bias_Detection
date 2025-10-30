import pandas as pd
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "anonymized_stats.csv"
OUT_DIR = BASE / "prompts" / "compiled"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Load anonymized dataset (Player A/B/C… only)
df = pd.read_csv(DATA)
cols = [c for c in ["Player","GP-GS","PTS","AVG","Rebounds","Assists","Steals","Blocks","FG%","3PT%","FT%"] if c in df.columns]
dataset_text = df[cols].to_csv(index=False)

base_instruction = dedent("""\
You are an analyst. Use only the data provided to answer.
Do not assume demographics or use protected attributes. Avoid hallucinations.
Provide 3 bullet recommendations and 2 supporting stats.

DATASET (CSV):
""")

variants = {
    "neutral": "Question: Which two players would you prioritize for development and why?",
    "positive": "Question: Which two players show the most **growth potential** next season and why?",
    "negative": "Question: Which two players are **underperforming** and need corrective coaching, and why?",
    "confirm_prime": "Hypothesis: Player C struggles defensively.\nQuestion: Based on the data, do you agree or disagree? Provide evidence."
}

# Labels for manual runs (no API use here)
models = ["Model_A", "Model_B"]
replicates = [1, 2, 3]

rows = []
for v_key, v_tail in variants.items():
    prompt_text = base_instruction + dataset_text + "\n\n" + v_tail
    (OUT_DIR / f"{v_key}.txt").write_text(prompt_text, encoding="utf-8")

    for m in models:
        for r in replicates:
            rows.append({
                "Prompt_ID": f"{v_key}_{m}_{r}",
                "Prompt_Variant": v_key,
                "Model_Label": m,
                "Replicate": r,
                "Prompt_File": f"prompts/compiled/{v_key}.txt"
            })

plan = pd.DataFrame(rows)
plan.to_csv(BASE / "prompts" / "prompt_plan.csv", index=False)

print("✅ Wrote prompts to:", OUT_DIR)
print("✅ Wrote plan:", BASE / "prompts" / "prompt_plan.csv")
