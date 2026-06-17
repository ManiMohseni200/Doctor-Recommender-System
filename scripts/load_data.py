import pandas as pd
from database_connection import get_engine

def load_doctors():
    engine = get_engine()
    df = pd.read_sql_table('Doctors', con=engine)
    return df

def load_reviews():
    engine = get_engine()
    df = pd.read_sql_table('Reviews', con=engine)
    return df

if __name__ == '__main__':
    doctors_df = load_doctors()
    reviews_df = load_reviews()
    print(f"Loaded {len(doctors_df)} doctors and {len(reviews_df)} reviews from database.")