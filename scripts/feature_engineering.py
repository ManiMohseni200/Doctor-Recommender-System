import pandas as pd
import os
from sentence_transformers import SentenceTransformer
import pickle

def create_features():
    df_doctors = pd.read_csv('data/cleaned_doctors.csv')
    df_reviews = pd.read_csv('data/cleaned_reviews.csv')

    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    
    reviews_text = df_reviews['Cleaned_Review'].astype(str).tolist()
    embeddings = model.encode(reviews_text, show_progress_bar=True)
    
    df_reviews['Embedding'] = list(embeddings)

    df_doctors['Region'] = df_doctors['Location'].apply(lambda x: x.split('،')[0] if pd.notna(x) else 'نامشخص')

    os.makedirs('features', exist_ok=True)
    
    with open('features/reviews_embeddings.pkl', 'wb') as f:
        pickle.dump(df_reviews, f)
        
    df_doctors.to_csv('features/doctors_features.csv', index=False)

if __name__ == '__main__':
    create_features()