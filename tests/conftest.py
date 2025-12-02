import pandas as pd
import pytest


@pytest.fixture
def sample_fx_data():
    data = {
        "date": [
            "2025-11-21",
            "2025-11-22",
            "2025-11-23",
            "2025-11-21",
            "2025-11-23",
            "2025-11-22",
        ],
        "currency_code": ["USD", "EUR", "EUR", "USD", "EUR", "USD"],
        "price_in_PLN_raw": [3.6933, 4.9002, 4.2444, 3.765, 4.521, 3.998],
    }
    data_df = pd.DataFrame(data)
    data_df["date"] = pd.to_datetime(data_df["date"])
    return data_df
