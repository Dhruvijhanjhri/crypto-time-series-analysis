import os
import pandas as pd

def load_forecast():
    # Get root directory of StreamlitApp
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build correct path
    file_path = os.path.join(base_dir, "data", "final_crypto_forecast_master.csv")

    # Debug print (optional but useful)
    print("Looking for file at:", file_path)

    # Read CSV
    df = pd.read_csv(file_path)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    return df