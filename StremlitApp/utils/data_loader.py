import os
import pandas as pd

def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "final_crypto_forecast_master.csv")
    
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    
    return df