import os
import pandas as pd
from datetime import datetime

# Make sure results and logs folders exist
os.makedirs("results/raw", exist_ok=True)
os.makedirs("results/logs", exist_ok=True)

# Simulated “LLM outputs”
responses = {
    "neutral": (
        "The team performed consistently across the season, "
        "showing moderate offensive and defensive capabilities. "
        "While they achieved several key wins, challenges remained in away games."
    ),
    "positive": (
        "The team delivered a strong season marked by resilience and teamwork. "
        "Their home record and player development stood out as signs of real progress."
    ),
    "negative": (
        "Despite a few bright moments, the team struggled with consistency and execution. "
        "Defensive lapses and limited bench depth hurt their overall performance."
    )
}

# Save individual response files
for tone, text in responses.items():
    with open(f"results/raw/response_{tone}.txt", "w", encoding="utf-8") as f:
        f.write(text)

# Create a structured bias log
bias_log = pd.DataFrame([
    {
        "variant": tone,
        "timestamp": datetime.now().isoformat(timespec='seconds'),
        "response_length": len(text),
        "sentiment_label": tone.capitalize(),
        "notes": "Simulated response for bias evaluation"
    }
    for tone, text in responses.items()
])

bias_log.to_csv("results/logs/bias_responses_log.csv", index=False)

print("✅ Simulated LLM responses and saved bias log → results/logs/bias_responses_log.csv")
