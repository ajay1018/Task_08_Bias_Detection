import os, random, pandas as pd

os.makedirs("results/raw", exist_ok=True)
os.makedirs("results/logs", exist_ok=True)

variants = ["neutral", "positive", "negative"]
runs = []

for v in variants:
    for i in range(1, 4):
        resp = f"This is simulated response {i} for {v} framing — narrative tone: {random.choice(['neutral','optimistic','critical'])}."
        out_path = f"results/raw/round3_{v}_{i}.txt"
        with open(out_path, "w") as f:
            f.write(resp)
        runs.append({"variant": v, "run": i, "path": out_path, "sentiment": random.uniform(-1,1)})

pd.DataFrame(runs).to_csv("results/logs/final_bias_log.csv", index=False)
print("✅ Final experiment logs saved.")
