import streamlit as st

st.title("📊 About Project — NBP Daily ETL & FX Data Explorer")

st.markdown(
    """
Welcome to the **NBP FX Dashboard**, an interactive application for exploring 
daily foreign exchange (FX) rates published by the **National Bank of Poland (NBP)**.

This dashboard is powered by a fully automated **End-to-End ETL pipeline**, built on:

- **Databricks**
- **Delta Lake (Unity Catalog)**
- **PySpark & Python**
- **GitHub API**
- **Streamlit**
- **Docker**

Every morning, the system fetches fresh FX data, cleans it, validates it, 
writes Silver & Gold Delta tables, and finally exports the dataset directly to GitHub —  
and this app displays the newest data automatically.
"""
)

# ---------------------------------------------
st.subheader("📈 What You Can Do on the Analytics Page")

st.markdown(
    """
On the Analytics page, you can:

1. **Pick one or many currencies**
2. **Choose a date range**
3. **View rate trends over time**
4. **Compare currencies side-by-side**
5. **Analyze daily % changes, rolling averages & volatility**
6. **Download the filtered dataset**

Everything is fully interactive — charts update instantly when you change filters.
"""
)

st.info("💡 Tip: Use the sidebar filters to customize your analysis in real time.")

# ---------------------------------------------
st.subheader("⚙️ Technologies Used")

st.markdown(
    """
- **Databricks** — runs the daily ETL pipeline  
- **Delta Lake (Unity Catalog)** — stores Source → Bronze → Silver → Gold tables  
- **PySpark / Python** — ingestion, transformations, validation  
- **GitHub API** — daily automated export of the Gold dataset  
- **Streamlit** — lightweight, fast analytics UI  
- **Docker** — packaging and deployment  
- **PyTest** — automated tests  
"""
)

# ---------------------------------------------
st.subheader("🎯 Purpose of This Project")

st.markdown(
    """
This project demonstrates how to build a **complete modern data engineering workflow**:

- How to ingest API data on a schedule  
- How to process and validate it at each ETL layer  
- How to design Bronze → Silver → Gold Delta tables  
- How to expose curated data to end users  
- How to integrate **Databricks + GitHub + Streamlit** into a single automated system  

The goal is to provide a simple, clean user experience, while showcasing strong 
**Data Engineering & Cloud skills**.
"""
)

# ---------------------------------------------
st.subheader("📌 About the Analytics Dashboard")

st.markdown(
    """
On the Analytics Dashboard, you can:

- select currencies  
- adjust date ranges  
- switch metrics (raw rate, % change, normalized index)  
- compare multiple currencies  
- explore interactive line charts  
- inspect raw data  
- download results  

This is the main space where you can freely explore the FX dataset.
"""
)

st.success(
    "🚀 You're all set! Go to *Analytics* in the sidebar to start exploring the FX data."
)


# # =============
# st.write("====================================================")
# st.write(
#     "This project consumes data each day rom Databricks ETL pipeline, using Medalion architecutre and pushed data to github everydatyu to imitade data source storage"
# )

# st.write(
#     "In this page you are able to select filters to explore the main data with only one choosen currency"
# )
# st.write("Plsease choose the time on how much you want to explore data")
# up_to_date = st.slider(
#     "Choose the date up to whitch you want to explore data", min_value=0, max_value=30
# )

# currency = st.selectbox("Choose major currency", ["EUR", "USD", "GBP", "CHF"])
# df_cur = df[df["currency_code"] == currency].sort_values("date")

# st.line_chart(df_cur, x="date", y="price_in_PLN_raw")

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
