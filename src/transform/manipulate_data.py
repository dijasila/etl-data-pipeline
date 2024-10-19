import pandas as pd

def manipulate_data(df):
    df['total_sales'] = df['quantity'] * df['price']
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/cleaned_sales_data.csv')
    manipulated_df = manipulate_data(df)
    manipulated_df.to_csv('../data/processed/manipulated_sales_data.csv', index=False)
    print("Data manipulated and saved to processed folder.")