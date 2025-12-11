import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from loguru import logger

from streamlit_app.functions.functions import filter_data, load_data

logger.info("User enetered analytics page")

try:
    df = load_data()
except Exception:
    st.stop()

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


seleected_currency = st.sidebar.multiselect(
    "Select currencies",
    options=all_currencies,
    default=default_currency,  # TODO write test if no currencies were choosen
)

if not seleected_currency:
    st.warning("Select Currency")
    st.stop()

date_range = st.sidebar.date_input(  # TODO check what happens if we have mistake
    "Select available time range",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date,
    format="YYYY/MM/DD",
)

if len(date_range) != 2:
    st.warning("Please select correct date")
    st.stop()


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


filtered_data = filter_data(
    data=df,
    selected_currencies=seleected_currency,
    date_range=(date_range),
    metric=metric_type,
)


wide_df_plot = filtered_data.pivot(
    index="date", columns="currency_code", values="metric"
)

if chart_type == "Line":
    st.line_chart(wide_df_plot)
elif chart_type == "Area":
    st.area_chart(wide_df_plot)
else:
    bar_chart = (
        alt.Chart(filtered_data)
        .mark_bar()
        .encode(
            x=alt.X("date_str:N", title="date"),
            xOffset=alt.XOffset("currency_code:N"),
            y=alt.Y("metric:Q", title="metric", stack=None),
            color=alt.Color("currency_code:N", title="currency"),
            tooltip=["date", "currency_code", "metric"],
        )
        .properties(
            height=400,
        )
    )

    st.altair_chart(bar_chart, width="stretch")
