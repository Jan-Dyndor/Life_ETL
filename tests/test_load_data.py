import base64
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest
from pandas import testing as pd_testing

from streamlit_app.functions.functions import load_data


@pytest.fixture
def github_data():
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
    # Github provides data as base64 encoded string
    # So  DataFrame -> bytes  -> base64 -> string
    data_df = pd.DataFrame(data)

    data_bytes = data_df.to_csv(index=False).encode()
    data_b64 = base64.b64encode(data_bytes)
    data_b64_string = data_b64.decode("utf-8")

    yield data_b64_string

    del data_b64_string


@pytest.fixture()
def fake_json_response(github_data):
    data = {"content": github_data}
    yield data


def test_download_data_happy(fake_json_response):
    with patch("streamlit_app.functions.functions.requests.get") as mock_get:
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.raise_for_status.side_effect = None
        fake_response.json.return_value = fake_json_response
        mock_get.return_value = fake_response

        df = load_data()
        expected = pd.Series(["USD", "EUR"])
        unique = pd.Series(df["currency_code"].unique())
        pd_testing.assert_series_equal(
            unique, expected, check_index=False, check_names=False
        )
        assert fake_response.status_code == 200

        assert fake_response.status_code == 200
