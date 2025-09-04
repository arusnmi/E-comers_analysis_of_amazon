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










# Plot for first level categories

# plt.figure(figsize=(12, 8))
# for category in df['first_category'].unique():
#     category_data = df[df['first_category'] == category]
#     plt.hist(category_data['discount_price_number'], bins=30, alpha=0.5, label=category)
# plt.ylabel('Frequency')
# plt.xlabel('Discounted Price')
# plt.title('Discounted Price Distribution by Main Category')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig('main_category_price_distribution.png')
# plt.show()

#  Plot for last level categories

# plt.figure(figsize=(12, 8))
# for category in df['last_category'].unique():
#     category_data = df[df['last_category'] == category]
#     plt.hist(category_data['discount_price_number'], bins=30, alpha=0.5, label=category)
# plt.ylabel('Frequency')
# plt.xlabel('Discounted Price')
# plt.title('Discounted Price Distribution by Sub Category')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig('sub_category_price_distribution.png')
# plt.show()



# 3D Scatter Plot of actual price, discount price, and discount percantage

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

for category in df['first_category'].unique():
    category_data = df[df['first_category'] == category]
    ax.scatter(category_data['actual_price_number'], 
              category_data['discount_price_number'],
              category_data['discount_percentage_number'],
              alpha=0.5,
              label=category)

ax.set_xlabel('Actual Price')
ax.set_ylabel('Discount Price')
ax.set_zlabel('Discount Percentage')
ax.set_title('3D Price Distribution by Main Category')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
plt.tight_layout()
plt.savefig('main_category_3d_scatter.png', bbox_inches='tight')
plt.show()

# 3D Scatter plot for last category
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

for category in df['last_category'].unique():
    category_data = df[df['last_category'] == category]
    ax.scatter(category_data['actual_price_number'], 
              category_data['discount_price_number'],
              category_data['discount_percentage_number'],
              alpha=0.5,
              label=category)

ax.set_xlabel('Actual Price')
ax.set_ylabel('Discount Price')
ax.set_zlabel('Discount Percentage')
ax.set_title('3D Price Distribution by Sub Category')
plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
plt.tight_layout()
plt.savefig('sub_category_3d_scatter.png', bbox_inches='tight')
plt.show()















