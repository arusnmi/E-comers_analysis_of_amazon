import pandas as pd

df=pd.read_csv('amazon_fixed_ratings.csv')



df ["discount_percentage_number"]= df["discount_percentage"].str.split('%').str[0].astype(int)

df.to_csv('amazon_discounts.csv', index=False)
