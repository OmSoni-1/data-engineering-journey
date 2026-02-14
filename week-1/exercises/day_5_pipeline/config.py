import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

DATA_YEAR = os.getenv("DATA_YEAR")
STATUS_FILTER = os.getenv("STATUS_FILTER")

if not DATA_YEAR:
    raise ValueError("DATA_YEAR not set")

if not STATUS_FILTER:
    raise ValueError("STATUS_FILTER not set")

try:
    DATA_YEAR = int(DATA_YEAR)
except ValueError:
    raise ValueError("DATA_YEAR must be numeric")