import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/sales_data.csv')
    clean_df = clean_data(df)
    clean_df.to_csv('../data/processed/cleaned_sales_data.csv', index=False)
    print("Data cleaned and saved to processed folder.")