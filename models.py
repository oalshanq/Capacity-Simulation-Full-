
import pandas as pd
import numpy as np

def run_simulation(region, specialty):
    years = list(range(2025, 2055))
    data = []
    for year in years:
        demand = np.random.randint(2000, 9000)
        beds = int(demand * 0.01)
        physicians = int(demand * 0.02)
        nurses = int(demand * 0.03)
        data.append({
            "Region": region,
            "Specialty": specialty,
            "Year": year,
            "Demand": demand,
            "Beds": beds,
            "Physicians": physicians,
            "Nurses": nurses
        })
    return pd.DataFrame(data)

def get_region_coords():
    return {
        "Riyadh": [24.7136, 46.6753],
        "Makkah": [21.3891, 39.8579],
        "Madinah": [24.5247, 39.5692],
        "Eastern Province": [26.4207, 50.0888],
        "Qassim": [26.2076, 43.4837],
        "Hail": [27.5114, 41.7208],
        "Tabuk": [28.3838, 36.5550],
        "Jouf": [29.9729, 40.9388],
        "Nothern Borders": [30.0342, 41.0340],
        "Baha": [20.0129, 41.4677],
        "Assir": [18.2479, 42.5117],
        "Najran": [17.4917, 44.1320],
        "Jizan": [16.8890, 42.5706]
    }
