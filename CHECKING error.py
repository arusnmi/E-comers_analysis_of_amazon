import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException


# Load CSV
df = pd.read_csv('amazon_fixed_ratings.csv')


# Split the user_name and user_id columns by commas
df['user_name'] = df['user_name'].str.split(',')
df['user_id'] = df['user_id'].str.split(',')
df['review_id'] = df['review_id'].str.split(',')
df['review_title'] = df['review_title'].str.split(',')
df['review_content'] = df['review_content'].str.split(',')
# Explode both columns so each element becomes its own row
cols_to_explode = ["user_id", "user_name", "review_id", "review_title", "review_content"]
df[cols_to_explode] = df[cols_to_explode].apply(lambda x: x.str.split(','))
df = df.explode(cols_to_explode)


# Reset index for cleanliness
df = df.reset_index(drop=True)


   


DetectorFactory.seed = 0
def detect_language(text):
    try:
        return detect(str(text)) if pd.notnull(text) else "unknown"
    except LangDetectException:
        return "unknown"

df = df[df["review_title"].apply(detect_language) == "en"]
df = df[df["review_content"].apply(detect_language) == "en"]


df.to_csv('amazon_fixed_ratings_cleaned.csv', index=False)