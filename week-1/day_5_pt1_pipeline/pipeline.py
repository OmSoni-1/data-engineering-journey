import pandas as pd
import pathlib as pl
from config import DATA_YEAR, STATUS_FILTER

BASE_DIR = pl.Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "output" / "regional_sales_summary.csv"

def extract_data(path: pl.Path) -> pd.DataFrame:
    return pd.read_csv(path)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["order_date"] = pd.to_datetime(df["order_date"])
    start_date = pd.to_datetime(f"{DATA_YEAR}-01-01")

    df = df[
        (df["status"] == STATUS_FILTER) &
        (df["order_date"] >= start_date)
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

def load_data(df: pd.DataFrame, path: pl.Path) -> None:
    df.to_csv(path, index=False)

def main():
    df = extract_data(INPUT_FILE)
    summary_df = transform_data(df)
    load_data(summary_df, OUTPUT_FILE)
    print("Regional Sales summary generated successfully!")

if __name__ == "__main__":
    main()