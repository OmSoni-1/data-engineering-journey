import pandas as pd
import pathlib as pl

BASE_DIR = pl.Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "output" / "regional_sales_summary.csv"

# Read data from the CSV present at the path and return is as a DataFrame #
def extract_data(path: pl.Path) -> pd.DataFrame:
    return pd.read_csv(path)

# Perform analysis and transformation. This step filters out the data and provide the intended one as a DataFrame #
def trannsform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])

    df = df[
        (df["status"] == "Completed") & 
        (df["order_date"] >= '2026-01-01')
    ]

    summary_df = (
        df.groupby("region")
        .agg(
            total_orders = ("order_id", "count"),
            total_quantity = ("quantity", "sum"),
            total_revenue = ("total_amount", "sum"),
            avg_order_value = ("total_amount", "mean")
        )
        .reset_index()
    )

    return summary_df

# This step basically stores the transformed data as a CSV to the provided path #
def load_data(df: pd.DataFrame, path: pl.Path) -> None:
    df.to_csv(path, index=False)

def main():
    df = extract_data(INPUT_FILE)
    summary_df = trannsform_data(df)
    load_data(summary_df, OUTPUT_FILE)
    print("Regional sales summary generated successfully.")

if __name__ == "__main__":
    main()