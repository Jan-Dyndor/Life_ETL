import pandas as pd
import pytest


@pytest.fixture
def sample_fx_data():
    data = {
        "date": [
            "2025-11-22",  # USD
            "2025-11-21",  # EUR
            "2025-11-23",  # USD
            "2025-11-22",  # EUR
            "2025-11-21",  # USD
            "2025-11-23",  # EUR
        ],
        "currency_code": [
            "USD",
            "EUR",
            "USD",
            "EUR",
            "USD",
            "EUR",
        ],
        "price_in_PLN_raw": [
            3.765,  # USD 22
            4.9002,  # EUR 21
            3.998,  # USD 23
            4.2444,  # EUR 22
            3.6933,  # USD 21
            4.521,  # EUR 23
        ],
    }
    data_df = pd.DataFrame(data)
    data_df["date"] = pd.to_datetime(data_df["date"])
    return data_df
