import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['date'], df['total_sales'])
    plt.title('Total Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('../../docs/sales_visualization.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/manipulated_sales_data.csv')
    visualize_data(df)