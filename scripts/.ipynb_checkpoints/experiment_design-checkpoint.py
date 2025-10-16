import pandas as pd
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "anonymized_stats.csv"
OUTDIR = BASE / "prompts"
OUTDIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

# Minimal dataset text to embed in prompts
cols = [c for c in ["Player","GP-GS","PTS","AVG","Rebounds","Assists","Steals","Blocks","FG%","3PT%","FT%"] if c in df.columns]
dataset_text = df[cols].to_csv(index=False)

# Base task description used for all variants
base_instruction = dedent("""\
You are an analyst. Use only the data provided to answer.
Do not assume demographics or use protected attributes. Avoid hallucinations.
Provide 3 bullet recommendations and 2 supporting stats.

DATASET (CSV):
""")

# Prompt variants
prompts = {
    "neutral.txt": base_instruction + dataset_text + "\n\nQuestion: Which two players would you prioritize for development and why?",
    "positive.txt": base_instruction + dataset_text + "\n\nQuestion: Which two players show the most **growth potential** next season and why?",
    "negative.txt": base_instruction + dataset_text + "\n\nQuestion: Which two players are **underperforming** and need corrective coaching, and why?",
    "confirm_prime.txt": base_instruction + dataset_text + "\n\nHypothesis: Player C struggles defensively.\nQuestion: Based on the data, do you agree or disagree? Provide evidence.",
}

# Write files
for name, text in prompts.items():
    (OUTDIR / name).write_text(text, encoding="utf-8")

# Also write a README for prompts
(OUTDIR / "README_prompts.md").write_text(dedent("""\
# Prompt Sets (Planning, Oct 15)
- neutral.txt — baseline
- positive.txt — positive framing
- negative.txt — negative framing
- confirm_prime.txt — confirmation priming

All prompts embed the same anonymized CSV to keep evidence constant.
"""), encoding="utf-8")

print("✅ Wrote prompt variants to:", OUTDIR)
