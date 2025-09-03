import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('amazon_cleaned_preped.csv')
print(df.info())



# #ratings vs discount percentage
# ratings = df['rating']
# discount_percentage = df['discount_percentage_number']

# plt.figure(figsize=(10, 6))
# plt.bar( ratings,discount_percentage)
# plt.ylabel('Discount Percentage')
# plt.xlabel('Ratings')
# plt.title('Ratings vs Discount Percentage')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('ratings_vs_discount_percentage.png')


# #price distribution
# discounts = df['discount_price_number']
# actuals = df['actual_price_number']

# plt.figure(figsize=(10, 6))
# plt.hist([discounts, actuals], bins=30, label=['Discounted Price', 'Actual Price'], alpha=0.7)
# plt.ylabel('Frequency')
# plt.xlabel('Price')
# plt.title('Price Distribution')
# plt.legend()
# plt.tight_layout()
# plt.savefig('price_distribution.png')



#category price distrubition 

categories = df['category'].unique()
plt.figure(figsize=(12, 8))
for category in categories:
    category_data = df[df['category'] == category]
    plt.hist(category_data['discount_price_number'], bins=30, alpha=0.5, label=category)
plt.ylabel('Frequency')
plt.xlabel('Discounted Price')
plt.title('Discounted Price Distribution by Category')
plt.legend()
plt.savefig('category_price_distribution.png')
plt.show()




















