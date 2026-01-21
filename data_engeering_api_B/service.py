import pandas as pd
import numpy as np
from schemas import WhetherLocation
import requests

def convert_data_to_df(data: dict):
    df = pd.read_(data)
    return df

def convert_type(df, column_name, new_type):
    df[column_name] = df[column_name].astype(new_type)
    return df



def add_temper_column(df):
    '''The function add status whether column'''
    df['temperature_category'] = pd.cut(
        df['temperature'],
        bins=[-np.inf, 18, 25],
        labels=["cold", "moderate", "hot"]
    )
    return df

def windy_column(df):
    df['wind_status'] = pd.cut(
        df['wind_speed'],
        bins=[0, 10, np.inf],
        labels=["windy", "calm"]
        include_lowest=True
    )
    return df


def save_data(data):
    url = "https://--------:8040/records"
    params = {'records': data}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()




def clean_data(data: WhetherLocation):
    df = convert_data_to_df(data)
    url = 