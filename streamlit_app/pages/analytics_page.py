import numpy as np
import pandas as pd
import streamlit as st
from functions.functions import load_data


df = (
    load_data()
)  # think about hwo to cache that and the needed below things to be faster becasue i will allways use it
all_currencies: np.ndarray = df["currency_code"].unique()
default_currency: list = ["USD", "EUR"]
number_of_days_in_df: int = len(df["date"].unique())
start_date: pd.Timestamp = df["date"].min()
end_date: pd.Timestamp = df["date"].max()


st.set_page_config(
    page_title="FX Analytics",
    page_icon="📊",
    layout="wide",
)

# ---------- SIDEBAR ----------
st.sidebar.header("Filters")


st.write("Welcome at Analitycs page! ")

tab_overview, tab_trends, tab_changes, tab_data = st.tabs(
    ["Overview", "Trends", "Changes & Volatility", "Data"]
)


seleected_currency = st.sidebar.multiselect(
    "Select currencies",
    options=all_currencies,
    default=default_currency,  # write test if no currencies were choosen
)


date_range = st.sidebar.date_input(  # check what happens if we have mistake
    "Select available time range",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date,
    format="YYYY/MM/DD",
)

metric_type = st.sidebar.selectbox(
    "Metric",
    options=[
        "Rate (PLN)",
        "Daily change in %",
        "Normalized index (start=100)",
    ],
)

chart_type = st.sidebar.radio(
    "Chart type",
    options=["Line", "Area", "Bar"],
    horizontal=True,
)

with st.sidebar.expander("Advanced options"):
    show_rolling = st.checkbox("Show rolling average")
    rolling_window = st.slider(
        "Rolling window (days)",
        min_value=3,
        max_value=number_of_days_in_df,
        value=7,
    )
    show_volatility = st.checkbox("Show volatility summary")
