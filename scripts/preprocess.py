import pandas as pd
import re
import os
from load_data import load_doctors, load_reviews

def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'[^\w\sآ-ی]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data():
    df_doctors = load_doctors()
    df_reviews = load_reviews()

    df_reviews['Cleaned_Review'] = df_reviews['Review_Text'].apply(clean_text)
    
    df_reviews = df_reviews[df_reviews['Cleaned_Review'] != ""]

    df_doctors.fillna('نامشخص', inplace=True)

    os.makedirs('data', exist_ok=True)
    df_doctors.to_csv('data/cleaned_doctors.csv', index=False)
    df_reviews.to_csv('data/cleaned_reviews.csv', index=False)
    
    print("Preprocessing complete. Cleaned data saved to 'data/' folder.")

if __name__ == '__main__':
    preprocess_data()