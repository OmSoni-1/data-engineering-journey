from pipeline import extract_data, transform_data, load_data
#import pipeline
from pathlib import Path

#print(dir(pipeline))

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "output" / "regional_sales_summary.csv"

def main():
    df = extract_data(INPUT_FILE)
    summary_df = transform_data(df)
    load_data(summary_df, OUTPUT_FILE)
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    main()