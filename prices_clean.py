import pandas as pd

df = pd.read_csv('amazon_discounts_cleaned.csv')

# Clean discounted_price -> float
df["discount_price_number"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)   # remove rupee symbol
    .str.replace(",", "", regex=False)   # remove commas
    .astype(float)
)

# Clean actual_price -> float
df["actual_price_number"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Optionally overwrite the original columns
df["discounted_price"] = df["discount_price_number"]
df["actual_price"] = df["actual_price_number"]

df.dropna()

df.to_csv("amazon_price_cleaned.csv", index=False)
