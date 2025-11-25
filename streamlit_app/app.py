import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/gold_table.csv")

st.title("NBP Life Data")
st.write(
    "This project consumes data each day rom Databricks ETL pipeline, using Medalion architecutre and pushed data to github everydatyu to imitade data source storage"
)

st.write(
    "In this page you are able to select filters to explore the main data with only one choosen currency"
)
st.write("Plsease choose the time on how much you want to explore data")
up_to_date = st.slider(
    "Choose the date up to whitch you want to explore data", min_value=0, max_value=30
)

currency = st.selectbox("Choose major currency", ["EUR", "USD", "GBP", "CHF"])
df_cur = df[df["currency_code"] == currency].sort_values("date")

st.line_chart(df_cur, x="date", y="price_in_PLN_raw")

# y_min = df_cur["price_in_PLN_raw"].min() - 0.05
# y_max = df_cur["price_in_PLN_raw"].max() + 0.05

# chart = (
#     alt.Chart(df_cur)
#     .mark_line(point=True)
#     .encode(
#         x="date",
#         y=alt.Y("price_in_PLN_raw", scale=alt.Scale(domain=[y_min, y_max])),
#         tooltip=["date", "price_in_PLN_raw"],
#     )
#     .interactive()
# )
# st.altair_chart(chart, use_container_width=True)
