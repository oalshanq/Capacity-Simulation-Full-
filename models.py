
import pandas as pd
import numpy as np

def load_real_supply_data():
    return pd.read_csv("real_supply_data.csv")

def simulate_with_real_supply(region, specialty, supply_df):
    np.random.seed(42)
    years = list(range(2025, 2055))
    base = {
        "Beds": 2.5,
        "Nurses": 6.0,
        "Clinics": 1.2,
        "Physicians": 3.3
    }
    modifier = hash(specialty) % 5 * 0.05 + 0.95
    row = supply_df[supply_df["Region"] == region].iloc[0]
    df = []

    for i, year in enumerate(years):
        growth = 1.01 ** i
        df.append({
            "Year": year,
            "Region": region,
            "Specialty": specialty,
            "Beds_Demand": round(base["Beds"] * modifier * growth, 2),
            "Beds_Supply": round(row["Beds_per_1k"], 2),
            "Nurses_Demand": round(base["Nurses"] * modifier * growth, 2),
            "Nurses_Supply": round(row["Nurses_per_1k"], 2),
            "Clinics_Demand": round(base["Clinics"] * modifier * growth, 2),
            "Clinics_Supply": round(row["Clinics_per_1k"], 2),
            "Physicians_Demand": round(base["Physicians"] * modifier * growth, 2),
            "Physicians_Supply": round(row["Physicians_per_1k"], 2)
        })
    return pd.DataFrame(df)
