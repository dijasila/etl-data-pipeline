# ETL Data Pipeline

This repository contains an ETL data processing pipeline that extracts data from a SQL database, transforms and cleans it, loads it back into a database, and visualizes the results.

## Repository Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for documenting the ETL process.
- `src/`: Source code for the ETL pipeline.
  - `extract/`: Data extraction scripts.
  - `transform/`: Data transformation scripts.
  - `load/`: Data loading scripts.
  - `visualization/`: Data visualization scripts.
- `docs/`: Contains generated visualizations.

## How to Run

1. Clone the repository.
2. Install required packages: `pip install pandas matplotlib sqlalchemy`
3. Run the scripts in the following order:
   - Extract: `python src/extract/extract_data.py`
   - Transform: 
     - Clean: `python src/transform/clean_data.py`
     - Manipulate: `python src/transform/manipulate_data.py`
   - Load: `python src/load/load_data.py`
   - Visualize: `python src/visualization/visualize_data.py`