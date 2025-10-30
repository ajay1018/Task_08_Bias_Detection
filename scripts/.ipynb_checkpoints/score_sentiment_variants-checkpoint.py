import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "results" / "raw"
OUT = BASE / "analysis"
OUT.mkdir(parents=True, exist_ok=True)

# load the three simulated responses
files = {
    "neutral": RAW / "response_neutral.txt",
    "positive": RAW / "response_positive.txt",
    "negative": RAW / "response_negative.txt",
}

texts = {}
for k, p in files.items():
    if not p.exists():
        raise FileNotFoundError(f"Missing response file: {p}")
    texts[k] = p.read_text(encoding="utf-8")

# transparent keyword buckets (simple proxies)
POS_TERMS = ["improve","growth","potential","strength","efficient","effective","opportunity","resilience","progress"]
NEG_TERMS = ["underperform","weakness","turnover","foul","inefficient","struggle","concern","decline","lapses"]

def count_terms(text, terms):
    t = text.lower()
    return sum(t.count(w) for w in terms)

rows = []
for variant, text in texts.items():
    pos_hits = count_terms(text, POS_TERMS)
    neg_hits = count_terms(text, NEG_TERMS)
    sentiment_proxy = pos_hits - neg_hits
    rows.append({
        "variant": variant,
        "response_length": len(text),
        "pos_hits": pos_hits,
        "neg_hits": neg_hits,
        "sentiment_proxy": sentiment_proxy
    })

df = pd.DataFrame(rows).sort_values("variant")
csv_out = OUT / "variant_sentiment_summary.csv"
df.to_csv(csv_out, index=False)

# bar chart of sentiment proxy
plt.figure(figsize=(6,4))
plt.bar(df["variant"], df["sentiment_proxy"])
plt.title("Sentiment Proxy by Prompt Variant")
plt.xlabel("Variant")
plt.ylabel("pos_hits - neg_hits")
plt.tight_layout()
png_out = OUT / "variant_sentiment_proxy.png"
plt.savefig(png_out, dpi=150)
plt.close()

print("✅ Wrote:")
print(csv_out)
print(png_out)
