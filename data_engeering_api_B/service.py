import pandas as pd
import numpy as np
from schemas import WhatherLocation
import requests



class DataProcess:

    @staticmethod
    def load_data_to_df(data: dict[list[dict]]):
        df = pd.DataFrame(data['data'])
        return df


    @staticmethod
    def convert_to_datetime(df, column_name):
        df[column_name] = pd.to_datetime(df[column_name])
        return df
    

    @staticmethod
    def remove_duplicate(df):
        df = df.drop_duplicates()
        return df
    

    @staticmethod
    def add_temper_column(df):
        '''The function add status whether column'''
        df['temperature_category'] = pd.cut(
            df['temperature'],
            bins=[-np.inf, 18, 25, np.inf],
            labels=["cold", "moderate", "hot"]
        )
        #df['temperature_category'] = df['temperature_category'].astype("object")
        return df


    @staticmethod
    def windy_column(df):
        df['wind_status'] = pd.cut(
            df['wind_speed'],
            bins=[0, 10, np.inf],
            labels=["windy", "calm"],
            include_lowest=True
        )
        #df['wind_status'] = df['wind_status'].astype("object")
        return df


    @staticmethod
    def save_data(data):
        url = "https://--------:8040/records"
        params = {'records': data}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


    @staticmethod
    def clean_data(data: WhatherLocation):
        df = DataProcess.load_data_to_df(data)
        df_clean_duplicate = DataProcess.remove_duplicate(df)
        #df_datetime = DataProcess.convert_to_datetime(df_clean_duplicate, "timestamp")
        df_temp_col = DataProcess.add_temper_column(df_clean_duplicate)
        windy_df = DataProcess.windy_column(df_temp_col)
        #url = DataProcess.save_data(df)
        return windy_df.to_json(orient="records")



data = {"data":
    [
        {
        "timestamp": "2026-01-19T00:00:00",
        "location_name": "Jerusalem",
        "country": "Israel",
        "latitude": 31.76904,
        "longitude": 35.21633,
        "temperature": 8.1,
        "wind_speed": 17.0,
        "humidity": 93
        }
 ]
 }

# x = DataProcess.clean_data(data)
# print(x)