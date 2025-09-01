import pandas as pd

df=pd.read_csv('amazon_discounts_cleaned.csv')



df ["discount_price_number"]= df['discounted_price'].str.split('â‚¹').str[0].astype(int)
df['discounted_price']=df['discounted_price'].str.split('â‚¹').str[0].astype(int)


df.to_csv('amazon_price_cleaned.csv',index=False)

