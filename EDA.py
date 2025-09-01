import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('amazon_discounts.csv')


ratings = df['rating']
discount_percentage = df['discount_percentage_number']

plt.figure(figsize=(10, 6))
plt.bar( ratings,discount_percentage)
plt.ylabel('Discount Percentage')
plt.xlabel('Ratings')
plt.title('Ratings vs Discount Percentage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ratings_vs_discount_percentage.png')





