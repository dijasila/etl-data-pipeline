import pandas as pd
from sqlalchemy import create_engine

def load_data(df, db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql('cleaned_sales', con=engine, if_exists='replace', index=False)
    print("Data loaded into the database.")

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/manipulated_sales_data.csv')
    load_data(df, '../data/processed/sales_data.db')