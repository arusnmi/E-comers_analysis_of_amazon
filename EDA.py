import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('amazon_cleaned_preped_split.csv')
# print(df.info())



# #ratings vs discount percentage


# plt.figure(figsize=(10, 6))
# sns.barplot(x='rating', y='discount_percentage_number', data=df)
# plt.ylabel('Discount Percentage')
# plt.xlabel('Ratings')
# plt.title('Average Discount Percentage by Rating')
# plt.xticks(rotation=45)

# plt.savefig('ratings_vs_discount_percentage.png')
# plt.show()










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

# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(111, projection='3d')

# for category in df['first_category'].unique():
#     category_data = df[df['first_category'] == category]
#     ax.scatter(category_data['actual_price_number'], 
#               category_data['discount_price_number'],
#               category_data['discount_percentage_number'],
#               alpha=0.5,
#               label=category)

# ax.set_xlabel('Actual Price')
# ax.set_ylabel('Discount Price')
# ax.set_zlabel('Discount Percentage')
# ax.set_title('3D Price Distribution by Main Category')
# plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig('main_category_3d_scatter.png', bbox_inches='tight')
# plt.show()

# 3D Scatter plot for last category


# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(111, projection='3d')

# for category in df['last_category'].unique():
#     category_data = df[df['last_category'] == category]
#     ax.scatter(category_data['actual_price_number'], 
#               category_data['discount_price_number'],
#               category_data['discount_percentage_number'],
#               alpha=0.5,
#               label=category)

# ax.set_xlabel('Actual Price')
# ax.set_ylabel('Discount Price')
# ax.set_zlabel('Discount Percentage')
# ax.set_title('3D Price Distribution by Sub Category')
# plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig('sub_category_3d_scatter.png', bbox_inches='tight')
# plt.show()



#RATING AVRAGE VS COUNT

# plt.figure(figsize=(10, 6))

# rating=df["rating"]
# rating_count=df["rating_count"]
# sns.barplot(x=rating, y=rating_count, data=df)
# plt.ylabel('Average Rating Count')
# plt.xlabel('Rating')
# plt.title('Average Rating Count by Rating')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('rating_count_by_average_rating.png')
# plt.show()


#Pie chart for diffent prouducts over catgroies 


# category_counts_first = df['first_category'].value_counts()
# catgroy_counts_last = df['last_category'].value_counts()
# prouduct_id=df['product_id'].unique()
# # Pie chart for first category
# plt.figure(figsize=(10, 8))
# plt.pie(category_counts_first, labels=category_counts_first.index, autopct='%1.1f%%', startangle=140)
# plt.title('Product Distribution by Main Category')
# plt.savefig('product_distribution_main_category.png')
# plt.show()
# # Pie chart for last category
# plt.figure(figsize=(10, 8))
# plt.pie(catgroy_counts_last, labels=catgroy_counts_last.index, autopct='%1.1f%%', startangle=140)
# plt.title('Product Distribution by Sub Category')
# plt.savefig('product_distribution_sub_category.png')
# plt.show()


#heatmap for corrlating discount price, actual price, rating , rsating count , catgrories

plt.figure(figsize=(10, 8))
correlation_matrix = df[['actual_price_number', 'discount_price_number', 'discount_percentage_number', 'rating', 'rating_count']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()

