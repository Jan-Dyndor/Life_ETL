import numpy as np
import pandas as pd


def load_data() -> pd.DataFrame:
    df = pd.read_csv("../data/gold_table.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


if __name__ == "__main__":
    load_data()  # Learn more about it !
