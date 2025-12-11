import pandas as pd
import streamlit as st
import requests
import base64
import io
from loguru import logger
from config.core import config

URL: str = (
    f"https://api.github.com/repos/Jan-Dyndor/Life_ETL/contents/data/{config.catalog.gold_table}.csv"
)


@st.cache_data(ttl=24 * 60 * 60)  # refresh every 24hours = new data in GitHub
def load_data() -> pd.DataFrame:
    logger.debug("Load Data function activated")
    try:
        result = requests.get(URL)
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        st.error("Issue occurred while downloading the data - see logs")
        logger.exception(f"Can not fetch data! {err}")
        raise
    encoded_data = result.json()["content"]
    bytes_data = base64.b64decode(encoded_data)
    str_data = bytes_data.decode("utf-8")
    df = pd.read_csv(io.StringIO(str_data))
    df["date"] = pd.to_datetime(df["date"])
    logger.debug("Data fetched successfully")
    return df


def filter_data(
    *, data: pd.DataFrame, selected_currencies: list, date_range: tuple, metric: str
) -> pd.DataFrame:
    logger.debug("Filter Data function activated")

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    df_filterd = data[data["currency_code"].isin(selected_currencies)]
    df_filterd = df_filterd[df_filterd["date"].between(start_date, end_date)]

    df_filterd = df_filterd.sort_values(["currency_code", "date"])

    df_filterd["date_str"] = df_filterd["date"].dt.strftime("%Y-%m-%d")  # type: ignore

    if metric == "Rate (PLN)":
        df_filterd["metric"] = df_filterd["price_in_PLN_raw"]
    elif metric == "Daily change in %":
        df_filterd["metric"] = (
            df_filterd.groupby("currency_code")["price_in_PLN_raw"].pct_change() * 100
        )  # % of the change day by day
    else:
        currency_first_value = df_filterd.groupby("currency_code")[
            "price_in_PLN_raw"
        ].transform("first")
        df_filterd["metric"] = (
            df_filterd["price_in_PLN_raw"] / currency_first_value * 100
        )
    logger.debug("Filter Data function run successful")
    return df_filterd
