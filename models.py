
import pandas as pd
import numpy as np

def simulate_demand_vbic(region, specialty):
    np.random.seed(42)
    years = list(range(2025, 2055))
    base_rate = {
        "Beds_per_1k": 2.5,
        "Nurses_per_1k": 6.0,
        "Outpatient_Clinics_per_1k": 1.2,
        "Physician_Clinics_per_1k": 1.5
    }

    # Modulate by specialty (example logic)
    specialty_modifier = hash(specialty) % 5 * 0.05 + 0.95  # Range ~0.95–1.15

    data = []
    for i, year in enumerate(years):
        multiplier = 1.01 ** i  # 1% annual change
        data.append({
            "Year": year,
            "Region": region,
            "Specialty": specialty,
            "Beds_per_1k": round(base_rate["Beds_per_1k"] * multiplier * specialty_modifier, 2),
            "Nurses_per_1k": round(base_rate["Nurses_per_1k"] * multiplier * specialty_modifier, 2),
            "Outpatient_Clinics_per_1k": round(base_rate["Outpatient_Clinics_per_1k"] * multiplier * specialty_modifier, 2),
            "Physician_Clinics_per_1k": round(base_rate["Physician_Clinics_per_1k"] * multiplier * specialty_modifier, 2)
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
