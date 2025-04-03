
import pandas as pd
import numpy as np

def simulate_demand(region, specialty):
    np.random.seed(42)
    years = list(range(2025, 2055))
    base_demand = np.random.randint(5000, 10000)
    data = []

    for i, year in enumerate(years):
        growth = 1.02 ** i
        demand = int(base_demand * growth)
        beds = int(demand * 0.0225)  # 22.5 beds per 10k people
        physicians = int(demand * 0.0331)
        nurses = int(demand * 0.0582)
        data.append({
            "Year": year,
            "Region": region,
            "Specialty": specialty,
            "Demand": demand,
            "Beds": beds,
            "Physicians": physicians,
            "Nurses": nurses
        })
    return pd.DataFrame(data)

def load_static_data():
    data = {
        'Indicator': [
            'Total Population (2024)',
            'Saudi Nationals (2024)',
            'Non-Saudi Residents (2024)',
            'Annual Population Growth Rate (2024)',
            'Elderly Population (60+)',
            'Hospital Beds per 10,000 Population (2019)',
            'Physicians and Dentists per 10,000 Population (2019)',
            'Nurses including Midwives per 10,000 Population (2019)',
            'Total Number of Nurses (2023)',
            'Obesity Rate among Adults (15+ years) (2023)',
            'Overweight Individuals (15+ years) (2023)',
            'Basic Healthcare Coverage (2024)',
            'Saudi Unemployment Rate (Q4 2024)'
        ],
        'Value': [
            35300280,
            19600000,
            15700000,
            '4.7%',
            '3.81%',
            22.5,
            33.1,
            58.2,
            235461,
            '23.1%',
            '45.1%',
            '95.9%',
            '7.0%'
        ]
    }
    return pd.DataFrame(data)
