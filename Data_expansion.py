import pandas as pd
import re

# Load the CSV file containing Amazon discount data
df = pd.read_csv("amazon_discounts.csv")

# Define columns that contain review-related information
review_cols = ["user_id", "user_name", "review_id", "review_title", "review_content"]

# Function to split comma-separated strings into lists
# Returns empty list for NaN values
def split_list(s):
    if pd.isna(s):
        return []
    # Split on commas and remove surrounding whitespace
    return [part.strip() for part in str(s).split(',')]

# Apply the split_list function to all review columns
for c in review_cols:
    df[c] = df[c].map(split_list)

# Function to ensure all lists in a row have the same length
# by truncating to the shortest list length
def truncate_row(row):
    # Get lengths of all lists in the row
    lengths = [len(row[c]) for c in review_cols]
    m = min(lengths) if lengths else 0
    if m == 0:
        # If any list is empty, set all lists to empty
        for c in review_cols:
            row[c] = []
        return row
    # Truncate all lists to minimum length
    for c in review_cols:
        row[c] = row[c][:m]
    return row

# Apply truncation to all rows
df = df.apply(truncate_row, axis=1)

# Remove rows that have no review data left
df = df[df[review_cols].applymap(len).sum(axis=1) > 0]

# Expand the dataframe by creating a new row for each review
df = df.explode(review_cols, ignore_index=True)

# Define patterns to identify corrupted text (mojibake)
_SUSPECT_SEQS = [
    'Ã', 'Â', 'â',        # Common UTF-8 to Latin-1 conversion artifacts
    'à¤', 'à¥',           # Devanagari script conversion artifacts
    'œ', 'ž', '™', '€'    # Additional problematic characters
]
# Regular expression to match repeated mojibake patterns
_MOJIBAKE_RE = re.compile(r'(?:Ã.|Â.|â.|à[¤¥¦§¨¯±]){2,}')

# Function to detect if text contains corrupted characters
def looks_mojibake(text: str) -> bool:
    if pd.isna(text):
        return False
    t = str(text)
    # Count occurrences of suspicious character sequences
    hits = sum(t.count(seq) for seq in _SUSPECT_SEQS)
    # Check for repeated mojibake patterns
    if _MOJIBAKE_RE.search(t):
        hits += 2
    # Return True if multiple suspicious patterns found
    return hits >= 2

# Create a mask for rows with corrupted text in title or content
mask_bad = df["review_title"].map(looks_mojibake) | df["review_content"].map(looks_mojibake)
# Remove corrupted rows and create clean dataset
df_clean = df[~mask_bad].copy()

# Save the cleaned dataset to a new CSV file
df_clean.to_csv("amazon_discounts_cleaned.csv", index=False)
print("Saved amazon_discounts_cleaned.csv with", len(df_clean), "rows")
