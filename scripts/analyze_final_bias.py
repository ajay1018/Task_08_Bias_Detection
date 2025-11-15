import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the log generated from final experiment
log_path = "results/logs/final_bias_log.csv"
df = pd.read_csv(log_path)

# Aggregate sentiment by framing variant
summary = df.groupby("variant")["sentiment"].agg(["mean", "std", "count"]).reset_index()

# Save summary table
os.makedirs("analysis", exist_ok=True)
summary_path = "analysis/final_bias_summary.csv"
summary.to_csv(summary_path, index=False)

print("📊 Summary table saved to:", summary_path)
print("\nSummary:\n", summary)

# ---- Visualization 1: Distribution of Sentiment ----
plt.figure(figsize=(8,5))
sns.boxplot(x="variant", y="sentiment", data=df, palette="Set2")
plt.title("Sentiment Distribution by Prompt Framing Variant")
plt.xlabel("Framing Variant")
plt.ylabel("Sentiment Score")
plt.tight_layout()
plt.savefig("analysis/final_sentiment_boxplot.png", dpi=300)
plt.close()

# ---- Visualization 2: Mean Sentiment Bar Chart ----
plt.figure(figsize=(8,5))
sns.barplot(x="variant", y="mean", data=summary, palette="Set3")
plt.title("Mean Sentiment Score by Variant")
plt.xlabel("Framing Variant")
plt.ylabel("Mean Sentiment")
plt.tight_layout()
plt.savefig("analysis/final_sentiment_means.png", dpi=300)
plt.close()

print("📈 Visualizations saved:")
print(" - analysis/final_sentiment_boxplot.png")
print(" - analysis/final_sentiment_means.png")
