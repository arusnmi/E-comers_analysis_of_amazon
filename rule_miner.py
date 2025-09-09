import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

# Read the CSV file
df = pd.read_csv('user_dataset_with_clusters.csv')
print(df['first_category'].unique())

# Create binary columns for features we want to analyze
def create_binary_columns(df):
    # Product category binary
    df['is_computer_accessories'] = df['first_category'].apply(lambda x: 1 if 'Computers&Accessories' in x else 0)
    df['is_electronics'] = df['first_category'].apply(lambda x: 1 if 'Electronics' in x else 0)
    df['is_home_kitchen'] = df['first_category'].apply(lambda x: 1 if 'Home&Kitchen' in x else 0)
    df['is_musical_insturment'] = df['first_category'].apply(lambda x: 1 if 'MusicalInstruments' in x else 0)
    df['is_toys_games'] = df['first_category'].apply(lambda x: 1 if 'Toys&Games' in x else 0)
    df['is_offic_prouducts'] = df['first_category'].apply(lambda x: 1 if 'OfficeProducts' in x else 0)
    df['is_home_improvement'] = df['first_category'].apply(lambda x: 1 if 'HomeImprovement' in x else 0)
    df['is_vehicle'] = df['first_category'].apply(lambda x: 1 if 'Car&Motorbike' in x else 0)
    df['is_health_personal_care'] = df['first_category'].apply(lambda x: 1 if 'Health&PersonalCare' in x else 0)
    
    # Rating ranges
    df['high_rating'] = df['rating'].apply(lambda x: 1 if x >= 4.0 else 0)
    df['medium_rating'] = df['rating'].apply(lambda x: 1 if 3.0 <= x < 4.0 else 0)
    df['low_rating'] = df['rating'].apply(lambda x: 1 if x < 3.0 else 0)
    
    # Discount ranges
    df['high_discount'] = df['discount_percentage_number'].apply(lambda x: 1 if x >= 60 else 0)
    df['medium_discount'] = df['discount_percentage_number'].apply(lambda x: 1 if 30 <= x < 60 else 0)
    df['low_discount'] = df['discount_percentage_number'].apply(lambda x: 1 if x < 30 else 0)
    
    # Price ranges
    df['low_price'] = df['actual_price_number'].apply(lambda x: 1 if x < 500 else 0)
    df['medium_price'] = df['actual_price_number'].apply(lambda x: 1 if 500 <= x < 1000 else 0)
    df['high_price'] = df['actual_price_number'].apply(lambda x: 1 if x >= 1000 else 0)


    return df

# Create binary columns
df_encoded = create_binary_columns(df)

# Select columns for analysis
columns_for_analysis = [
    'is_computer_accessories', 'is_electronics', 'is_home_kitchen', 
    'is_musical_insturment', 'is_toys_games', 'is_offic_prouducts',
    'is_home_improvement', 'is_vehicle', 'is_health_personal_care',
    'high_rating', 'medium_rating', 'low_rating',
    'high_discount', 'medium_discount', 'low_discount',
    'low_price', 'medium_price', 'high_price'
]

# Generate frequent itemsets
frequent_itemsets = apriori(df_encoded[columns_for_analysis], 
                          min_support=0.05,  # Lowered minimum support due to more features
                          use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, 
                        metric="confidence",
                        min_threshold=0.5)  # Lower confidence threshold

# Sort rules by lift
rules = rules.sort_values('lift', ascending=False)

# Print results
print("\nNumber of frequent itemsets found:", len(frequent_itemsets))
print("\nTop 10 association rules by lift:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))