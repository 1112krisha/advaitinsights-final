# utils/data_loader.py
import pandas as pd

def get_data_from_csv(path="data/insights_data.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Company Name", "What Happened", "Date", "Category", "Priority",
            "Insight Type", "AI Summary", "Advait Angle", "Source Link"
        ])
