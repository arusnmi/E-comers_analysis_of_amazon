import pandas as pd
import numpy as np

df = pd.read_csv('amazon_cleaned_preped_split.csv')

print(df["user_id"].nunique())

#fequrency coloum - counting number of purchases per user
feq = df.groupby('user_id').size().reset_index(name='frequency')
df = df.merge(feq, on='user_id', how='left')    

#monetry_value coloum - summing total amount spent per user
monetary = df.groupby('user_id')['discounted_price'].sum().reset_index(name='monetary_value')
df = df.merge(monetary, on='user_id', how='left')

#unique products coloum - counting unique products bought per user
unique_products = df.groupby('user_id')['product_id'].nunique().reset_index(name='unique_products')
df = df.merge(unique_products, on='user_id', how='left')

#review_count_individual coloum - counting total reviews made by each user
review_count = df.groupby('user_id')['rating'].count().reset_index(name='review_count_individual')
df = df.merge(review_count, on='user_id', how='left')

#avrage_rating_individual coloum - calculating average rating given by each user
avg_rating = df.groupby('user_id')['rating'].mean().reset_index(name='average_rating_individual')
df = df.merge(avg_rating, on='user_id', how='left')

#avrage_discount_indv_product coloum - calculating average discount availed by each user
avg_discount = df.groupby('user_id')['discounted_price'].mean().reset_index(name='average_discount_individual_product')
df = df.merge(avg_discount, on='user_id', how='left')

# Display the updated DataFrame
print(df.head())
df.to_csv('user_dataset.csv', index=False)


 