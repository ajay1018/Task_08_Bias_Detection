import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
raw_csv = BASE / "results" / "raw" / "collection_template.csv"
out_dir = BASE / "analysis"
out_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw_csv)
df["Response_Text"] = df["Response_Text"].fillna("").astype(str)

# Transparent keyword buckets (simple proxies)
POS_TERMS = ["improve","growth","potential","strength","efficient","effective","opportunity"]
NEG_TERMS = ["underperform","weakness","turnover","foul","inefficient","struggle","concern","decline"]
OFF_TERMS = ["points","scoring","shooting","3pt","fg%","ft%","assist","offense"]
DEF_TERMS = ["steal","block","rebound","defense","defensive","turnover","foul"]

def count_terms(text, terms):
    t = text.lower()
    return sum(t.count(w) for w in terms)

df["pos_hits"] = df["Response_Text"].apply(lambda t: count_terms(t, POS_TERMS))
df["neg_hits"] = df["Response_Text"].apply(lambda t: count_terms(t, NEG_TERMS))
df["off_hits"] = df["Response_Text"].apply(lambda t: count_terms(t, OFF_TERMS))
df["def_hits"] = df["Response_Text"].apply(lambda t: count_terms(t, DEF_TERMS))
df["sentiment_proxy"] = df["pos_hits"] - df["neg_hits"]

# Confirmation-primed agreement (very simple heuristic)
def confirm_agree(text):
    t = text.lower()
    if "agree" in t and "disagree" not in t: return 1
    if "disagree" in t and "agree" not in t: return 0
    if "support" in t and "refute" not in t: return 1
    if "refute" in t and "support" not in t: return 0
    return None

df["confirm_agree_flag"] = df.apply(
    lambda r: confirm_agree(r["Response_Text"]) if r["Prompt_Variant"]=="confirm_prime" else None,
    axis=1
)

# Aggregate: averages by variant/model
agg = df.groupby(["Prompt_Variant","Model_Label"], dropna=False).agg({
    "sentiment_proxy":"mean",
    "pos_hits":"mean",
    "neg_hits":"mean",
    "off_hits":"mean",
    "def_hits":"mean",
    "confirm_agree_flag":"mean"
}).reset_index()

# Write outputs
detailed_out = out_dir / "scored_responses_detailed.csv"
summary_out  = out_dir / "variant_model_summary.csv"
df.to_csv(detailed_out, index=False)
agg.to_csv(summary_out, index=False)

print("✅ Wrote:")
print(summary_out)
print(detailed_out)
