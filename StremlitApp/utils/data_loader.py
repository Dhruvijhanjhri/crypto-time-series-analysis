import os
import pandas as pd

MASTER_FILE = "final_crypto_forecast_master.csv"

def load_forecast():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    path = os.path.join(DATA_DIR, MASTER_FILE)

    if not os.path.exists(path):
        raise FileNotFoundError(f"{MASTER_FILE} not found at {path}")

    df = pd.read_csv(path)
    return df