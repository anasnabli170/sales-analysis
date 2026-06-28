import pandas as pd
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, "data", "sales_data.csv")


def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["unit_price"])
    df = df.drop_duplicates()
    df["region"] = df["region"].str.title()
    df["product"] = df["product"].str.title()
    return df
