from streamlit_app.functions.functions import filter_data
import pandas as pd


def test_filter_data_filter_by_currency(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-22")
    metric: str = "Rate (PLN)"

    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )

    assert data_frame["currency_code"].unique() == selected_currency


def test_filter_data_filter_by_date(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-22")
    metric: str = "Rate (PLN)"

    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )
    min_date = pd.to_datetime(date_range[0])
    max_date = pd.to_datetime(date_range[1])

    assert data_frame["date"].min() == min_date
    assert data_frame["date"].max() == max_date
