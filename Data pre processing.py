import pandas as pd

# Read the original CSV file containing Amazon data
df = pd.read_csv('amazon.csv')

# Remove rows with missing values (NA/NaN)
new_df = df.dropna()

# Save the cleaned dataset without missing values
new_df.to_csv('amazon.csv_droped_na', index=False)

# Extract the rating column for further processing
rate = new_df['rating']

# Clean the ratings data:
# 1. Remove entries with '|' character
# 2. Remove ratings outside valid range (0-5)
for i in rate:
    if i == "|":
        # Remove rows where rating is '|'
        new_df_fixed = new_df.drop(new_df[new_df['rating'] == i].index)
    elif float(i) < 0.0 and float(i) > 5.0:
        # Remove rows where rating is outside 0-5 range
        new_df_fixed = new_df.drop(new_df[new_df['rating'] == i].index)
    else:
        print("ok")

# Save the final cleaned dataset with fixed ratings
new_df_fixed.to_csv('amazon.csv_fixed_ratings', index=False)