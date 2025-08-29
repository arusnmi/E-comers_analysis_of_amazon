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
df = df.explode('user_name').explode('user_id').explode('review_id').explode('review_title').explode('review_content')


# Reset index for cleanliness
df = df.reset_index(drop=True)








df=df.dropna()








DetectorFactory.seed = 0
def detect_language(text):
    try:
        return detect(str(text)) if pd.notnull(text) else "unknown"
    except LangDetectException:
        return "unknown"
   


df["lang_title"] = df["review_title"].apply(detect_language)
df["lang_content"] = df["review_content"].apply(detect_language)


df = df[df["lang_title"] == "en"].drop(columns=["lang_title"])
df = df[df["lang_content"] == "en"].drop(columns=["lang_content"])


df=df.drop(columns=["lang_title","lang_content"])


df.to_csv('amazon_fixed_ratings_cleaned.csv', index=False)