import pandas as pd

df = pd.read_csv('amazon_cleaned_preped.csv')
df= df.drop(df[df['rating']>5].index)
df.to_csv('amazon_cleaned_preped_no_outliers.csv', index=False)