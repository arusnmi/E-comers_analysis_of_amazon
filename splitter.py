import pandas as pd

df=pd.read_csv('amazon_price_cleaned.csv')



# df ["discount_percentage_number"]= df["discount_percentage"].str.split('%').str[0].astype(int)

# df.to_csv('amazon_discounts.csv', index=False)


import pandas as pd

df=pd.read_csv('amazon_price_cleaned.csv')



# df ["discount_percentage_number"]= df["discount_percentage"].str.split('%').str[0].astype(int)

# df.to_csv('amazon_discounts.csv', index=False)


df["category"]=df["category"].str.split('|')

df["first_category"]=df["category"].str[0]
df["last_category"]=df["category"].str[-1]
df.to_csv('amazon_cleaned_preped.csv', index=False)