import pandas as pd
from database_connection import get_engine

def import_data(csv_path):
    engine = get_engine()
    df = pd.read_csv(csv_path)

    doctors_df = df[['Name', 'Specialty', 'Location', 'Satisfaction Rate']].copy()
    doctors_df['Satisfaction Rate'] = pd.to_numeric(doctors_df['Satisfaction Rate'].astype(str).str.replace('%', ''), errors='coerce').fillna(0).astype(int)
    doctors_df.index += 1
    doctors_df.index.name = 'Doctor_ID'
    doctors_df.to_sql('Doctors', con=engine, if_exists='replace', index=True)

    reviews_list = []
    for idx, row in df.iterrows():
        doc_id = idx + 1
        if pd.isna(row['Reviews']):
            continue
        reviews_raw = str(row['Reviews']).split(' | ')
        for rev in reviews_raw:
            if ' :: ' in rev:
                parts = rev.split(' :: ')
                text = parts[0].strip()
                score_str = parts[1].replace('%', '').strip()
                try:
                    score = int(score_str)
                except ValueError:
                    score = 0
                reviews_list.append({'Doctor_ID': doc_id, 'Review_Text': text, 'Review_Score': score})

    reviews_df = pd.DataFrame(reviews_list)
    if not reviews_df.empty:
        reviews_df.index += 1
        reviews_df.index.name = 'Review_ID'
        reviews_df.to_sql('Reviews', con=engine, if_exists='replace', index=True)

if __name__ == '__main__':
    import_data('data/doctors_data.csv')