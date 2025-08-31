
import pandas as pd
import re

# === Load ===
df = pd.read_csv("amazon_discounts.csv")

review_cols = ["user_id", "user_name", "review_id", "review_title", "review_content"]

# --- Split into lists (simple comma split) ---
def split_list(s):
    if pd.isna(s):
        return []
    # split and strip surrounding spaces
    return [part.strip() for part in str(s).split(',')]

for c in review_cols:
    df[c] = df[c].map(split_list)

# --- Truncate to the shortest length per row so lists stay aligned ---
def truncate_row(row):
    lengths = [len(row[c]) for c in review_cols]
    m = min(lengths) if lengths else 0
    if m == 0:
        # nothing usable in this row
        for c in review_cols:
            row[c] = []
        return row
    for c in review_cols:
        row[c] = row[c][:m]
    return row

df = df.apply(truncate_row, axis=1)

# Drop rows where no reviews remain
df = df[df[review_cols].applymap(len).sum(axis=1) > 0]

# --- Explode all review columns together (prevents cartesian blow-up) ---
df = df.explode(review_cols, ignore_index=True)

# --- Remove corrupted/mojibake-looking entries ---
# Heuristics that catch typical UTF-8→Latin-1 mojibake like: Ã, Â, â, à¤, à¥, â€…
_SUSPECT_SEQS = [
    'Ã', 'Â', 'â',        # common crossover bytes
    'à¤', 'à¥',           # Devanagari bytes seen as Latin-1 (matches your example)
    'œ', 'ž', '™', '€'    # often appear in mojibake clusters
]
_MOJIBAKE_RE = re.compile(r'(?:Ã.|Â.|â.|à[¤¥¦§¨¯±]){2,}')

def looks_mojibake(text: str) -> bool:
    if pd.isna(text):
        return False
    t = str(text)
    # count hits of suspicious sequences
    hits = sum(t.count(seq) for seq in _SUSPECT_SEQS)
    # also catch repeating patterns like "à¤" / "â€"
    if _MOJIBAKE_RE.search(t):
        hits += 2
    # require more than one hit to avoid false positives; emojis and | / \ are fine
    return hits >= 2

mask_bad = df["review_title"].map(looks_mojibake) | df["review_content"].map(looks_mojibake)
df_clean = df[~mask_bad].copy()

df_clean.to_csv("amazon_discounts_cleaned.csv", index=False)
print("Saved amazon_discounts_cleaned.csv with", len(df_clean), "rows")
