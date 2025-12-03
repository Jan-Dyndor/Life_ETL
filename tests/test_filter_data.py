import pandas as pd
from pandas import testing as pandas_testing

from streamlit_app.functions.functions import filter_data


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


def test_filter_data_metric_rate(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-23")
    metric: str = "Rate (PLN)"

    expected_output = pd.Series([3.6933, 3.765, 3.998], name="metric")

    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )

    pandas_testing.assert_series_equal(
        expected_output, data_frame["metric"], check_index=False
    )


def test_filter_data_metric_daily_change(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-23")
    metric: str = "Daily change in %"

    expected_output = pd.Series([None, 1.941353, 6.188579], name="metric")
    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )

    pandas_testing.assert_series_equal(
        expected_output, data_frame["metric"], check_index=False
    )


def test_fiter_data_metric_normal(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-23")
    metric: str = "Normalized index (start=100)"

    expected_output = pd.Series(
        [100, 101.941353, 108.250074],
        name="metric",
    )
    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )

    pandas_testing.assert_series_equal(
        expected_output, data_frame["metric"], check_index=False
    )


def test_filter_data_metric_normal(sample_fx_data):
    selected_currency: list[str] = ["USD"]
    date_range: tuple = ("2025-11-21", "2025-11-23")
    metric: str = "Rate (PLN)"

    expected_output = pd.Series([3.6933, 3.765, 3.998], name="metric")

    data_frame = filter_data(
        data=sample_fx_data,
        selected_currencies=selected_currency,
        date_range=date_range,
        metric=metric,
    )

    pandas_testing.assert_series_equal(
        expected_output, data_frame["metric"], check_index=False
    )
