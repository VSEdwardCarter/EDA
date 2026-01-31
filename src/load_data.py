import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/yellow_tripdata_2023-01.parquet")

def load_data() -> pd.DataFrame:
    df = pd.read_parquet(DATA_PATH)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
    print(df.shape)
    print(df.info())
