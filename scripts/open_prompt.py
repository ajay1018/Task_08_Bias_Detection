import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
plan = pd.read_csv(BASE / "prompts" / "prompt_plan.csv")

def show_prompt(prompt_id: str):
    row = plan[plan["Prompt_ID"] == prompt_id]
    if row.empty:
        raise ValueError(f"Prompt_ID not found: {prompt_id}")
    row = row.iloc[0]
    text = (BASE / row["Prompt_File"]).read_text(encoding="utf-8")
    print("=" * 80)
    print("Prompt_ID:", row["Prompt_ID"])
    print("Variant:", row["Prompt_Variant"], "| Model_Label:", row["Model_Label"], "| Replicate:", row["Replicate"])
    print("=" * 80)
    print(text)

if __name__ == "__main__":
    # Example usage (change to any ID from prompts/prompt_plan.csv)
    show_prompt("neutral_Model_A_1")
