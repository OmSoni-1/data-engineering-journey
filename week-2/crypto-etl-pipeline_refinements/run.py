# run.py - Entry point for the ETL pipeline

from pipeline import run_pipeline
import sys

if __name__ == "__main__":
    print("\n🚀 Starting Crypto Price Tracker ETL Pipeline...\n")

    success = run_pipeline()

    if success:
        print("\n✅ Pipeline executed successfully!")
        print("Check logs/ folder for detailed execution log")
        sys.exit()
    else:
        print("\n❌ Pipeline failed. Check logs for details.")
        sys.exit(1)