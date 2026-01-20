import pandas as pd

def convert_to_df(data):
    df = pd.read_json(data)
    return df