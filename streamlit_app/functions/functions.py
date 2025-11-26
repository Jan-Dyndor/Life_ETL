import pandas as pd


def load_data() -> pd.DataFrame:
    df = pd.read_csv("../data/gold_table.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def filter_data(
    *, data: pd.DataFrame, selected_currencies: list, date_range: tuple, metric: str
) -> pd.DataFrame:

    df_filterd = data[data["currency_code"].isin(selected_currencies)]
    df_filterd = df_filterd[df_filterd["date"].between(date_range[0], date_range[1])]

    df_filterd = df_filterd.sort_values(["currency_code", "date"])

    if metric == "Rate (PLN)":
        df_filterd["metric_value"] = df_filterd["price_in_PLN_raw"]
    elif metric == "Daily change in %":
        df_filterd["metric_value"] = (
            df_filterd.groupby("currency_code")["price_in_PLN_raw"].pct_change() * 100
        )  # % of the change day by day
    else:
        currency_first_value = df_filterd.groupby("currency_code")[
            "price_in_PLN_raw"
        ].transform("first")
        df_filterd["metric_value"] = (
            df_filterd["price_in_PLN_raw"] / currency_first_value * 100
        )
    return df_filterd


if __name__ == "__main__":
    load_data()  # Learn more about it !
