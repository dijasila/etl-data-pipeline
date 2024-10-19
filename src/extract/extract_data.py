import pandas as pd
import sqlite3

def extract_data(db_path):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM sales"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    data = extract_data('../data/raw/sales_data.db')
    data.to_csv('../data/processed/sales_data.csv', index=False)
    print("Data extracted and saved to processed folder.")