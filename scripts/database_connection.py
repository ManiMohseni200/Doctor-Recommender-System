from sqlalchemy import create_engine

def get_engine(db_path='sqlite:///database/dataset.db'):
    engine = create_engine(db_path)
    return engine