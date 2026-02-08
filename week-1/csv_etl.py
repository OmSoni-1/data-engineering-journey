import pandas as pd
import pathlib as pl

# This is to make the paths dynamic #

BASE_DIR = pl.Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "output" / "filtered_sales.csv"

# Extraction step #
def extract_data(path: pl.Path) -> pd.DataFrame:
    return pd.read_csv(path)

#Transformation step #
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])

    filtered_df = df[
        (df["order_date"] >= '2026-01-20')
        &
        (df["status"] == "Completed")
    ]

    return filtered_df

#Load step: Loading the filtered data into a CSV #
def load_data(df: pd.DataFrame, path: pl.Path) -> None:
    df.to_csv(path, index=False)

def main():
    df = extract_data(INPUT_FILE)
    transformed_df = transform_data(df)
    load_data(transformed_df, OUTPUT_FILE)
    print("ETL process has been completed successfully!")

if __name__ == "__main__":
    main()