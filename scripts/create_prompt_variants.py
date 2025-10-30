import os, pandas as pd

os.makedirs("prompts/variants", exist_ok=True)

base_question = "Summarize the team’s 2023–24 basketball season performance using the provided metrics."

variants = {
    "neutral": f"{base_question} Provide an objective summary with factual focus only.",
    "positive": f"{base_question} Emphasize team achievements and strengths while maintaining credibility.",
    "negative": f"{base_question} Focus on weaknesses and areas needing major improvement."
}

for label, text in variants.items():
    with open(f"prompts/variants/prompt_{label}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("✅ Created prompt variants in prompts/variants/")
