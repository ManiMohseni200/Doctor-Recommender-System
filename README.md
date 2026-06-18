# Doctor Recommender System - AI Pipeline

This project implements an automated Data Science pipeline to process doctors' data and patient reviews, preparing them for a Recommender System using advanced NLP techniques.

## Pipeline Architecture
1. **Database Import (`import_to_db.py`)**: Parses raw CSV data, splits reviews, and imports them into a relational SQLite database.
2. **Preprocessing (`preprocess.py`)**: Loads data from SQLite and cleans the text by removing noise and special characters.
3. **Feature Engineering (`feature_engineering.py`)**: Uses `sentence-transformers` (paraphrase-multilingual-MiniLM-L12-v2) to generate semantic embeddings from the cleaned reviews.

## How to Run
Ensure you have Python 3.12+ installed. 

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
