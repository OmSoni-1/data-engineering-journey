import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from pipeline import transform_data

def test_transform_returns_dataframe():
    data = {
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "status": ["Completed"],
        "region": ["North"],
        "quantity": [2],
        "total_amount": [500]
    }

    df = pd.DataFrame(data)
    result = transform_data(df)

    assert isinstance(result, pd.DataFrame)

def test_filter_excludes_wrong_status():
    data = {
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "status": ["Cancelled"],
        "region": ["North"],
        "quantity": [2],
        "total_amount": [500]
    }

    df = pd.DataFrame(data)
    result = transform_data(df)

    assert result.empty