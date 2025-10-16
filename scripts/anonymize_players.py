import pandas as pd
from pathlib import Path
import string

# Paths (edit the INPUT to your actual Task 05 clean CSV path)
INPUT = Path(r"D:\Python_ws\RA-Syracuse\Task_05_Descriptive_Stats\data\basketball_2023_clean.csv")
BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "data" / "anonymized_stats.csv"
MAP_OUT = BASE / "data" / "anonymization_map.csv"

df = pd.read_csv(INPUT)

# Require minimal columns (adapt if yours differ)
keep_cols = [c for c in [
    "Player","GP-GS","PTS","AVG","Rebounds","Assists","Steals","Blocks","FG%","3PT%","FT%"
] if c in df.columns]
df = df[keep_cols].copy()

# Build deterministic mapping Player -> Player A/B/C...
unique_players = sorted(df["Player"].dropna().unique(), key=lambda x: str(x))
labels = [f"Player {letter}" for letter in string.ascii_uppercase]
if len(unique_players) > len(labels):
    labels += [f"Player {i}" for i in range(len(unique_players)-len(labels))]

mapping = dict(zip(unique_players, labels[:len(unique_players)]))
df["Player"] = df["Player"].map(mapping)

# Save anonymized CSV & mapping (mapping stays local or in docs WITHOUT real names if needed)
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

# Optional: write mapping file into data/ but redact the real names if you plan to commit it
map_df = pd.DataFrame(
    [{"real_name": k, "anon_id": v} for k, v in mapping.items()]
)
map_df.to_csv(MAP_OUT, index=False)

print(f"✅ Anonymized CSV: {OUT}")
print(f"ℹ️ Map CSV (review before committing): {MAP_OUT}")
