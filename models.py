
import pandas as pd
import numpy as np

def simulate_demand_supply_vbic(region, specialty):
    np.random.seed(42)
    years = list(range(2025, 2055))
    base_demand = {
        "Beds": 2.5,
        "Nurses": 6.0,
        "Outpatient_Clinics": 1.2,
        "Physicians": 3.3
    }
    base_supply = {
        "Beds": 2.1,
        "Nurses": 5.2,
        "Outpatient_Clinics": 1.0,
        "Physicians": 2.8
    }
    modifier = hash(specialty) % 5 * 0.05 + 0.95
    df = []

    for i, year in enumerate(years):
        multiplier = 1.01 ** i
        df.append({
            "Year": year,
            "Region": region,
            "Specialty": specialty,
            "Beds_Demand": round(base_demand["Beds"] * modifier * multiplier, 2),
            "Beds_Supply": round(base_supply["Beds"], 2),
            "Nurses_Demand": round(base_demand["Nurses"] * modifier * multiplier, 2),
            "Nurses_Supply": round(base_supply["Nurses"], 2),
            "Outpatient_Clinics_Demand": round(base_demand["Outpatient_Clinics"] * modifier * multiplier, 2),
            "Outpatient_Clinics_Supply": round(base_supply["Outpatient_Clinics"], 2),
            "Physicians_Demand": round(base_demand["Physicians"] * modifier * multiplier, 2),
            "Physicians_Supply": round(base_supply["Physicians"], 2)
        })
    return pd.DataFrame(df)

def all_regions_forecast(specialties):
    regions = ["Riyadh", "Makkah", "Madinah", "Eastern Province", "Qassim", "Hail",
               "Tabuk", "Jouf", "Nothern Borders", "Baha", "Assir", "Najran", "Jizan"]
    results = []
    for region in regions:
        row = {"Region": region}
        for spec in specialties:
            df = simulate_demand_supply_vbic(region, spec)
            gap = ((df.iloc[-1]["Beds_Demand"] + df.iloc[-1]["Nurses_Demand"] +
                    df.iloc[-1]["Outpatient_Clinics_Demand"] + df.iloc[-1]["Physicians_Demand"]) -
                   (df.iloc[-1]["Beds_Supply"] + df.iloc[-1]["Nurses_Supply"] +
                    df.iloc[-1]["Outpatient_Clinics_Supply"] + df.iloc[-1]["Physicians_Supply"]))
            row[spec] = round(gap, 2)
        results.append(row)
    return pd.DataFrame(results)

def specialty_summary(specialties, regions):
    summary = []
    for spec in specialties:
        beds_gap, nurses_gap, clinics_gap, physicians_gap = 0, 0, 0, 0
        for region in regions:
            df = simulate_demand_supply_vbic(region, spec)
            beds_gap += df.iloc[-1]["Beds_Demand"] - df.iloc[-1]["Beds_Supply"]
            nurses_gap += df.iloc[-1]["Nurses_Demand"] - df.iloc[-1]["Nurses_Supply"]
            clinics_gap += df.iloc[-1]["Outpatient_Clinics_Demand"] - df.iloc[-1]["Outpatient_Clinics_Supply"]
            physicians_gap += df.iloc[-1]["Physicians_Demand"] - df.iloc[-1]["Physicians_Supply"]
        n = len(regions)
        summary.append({
            "Specialty": spec,
            "Beds_Gap": round(beds_gap / n, 2),
            "Nurses_Gap": round(nurses_gap / n, 2),
            "Clinics_Gap": round(clinics_gap / n, 2),
            "Physicians_Gap": round(physicians_gap / n, 2)
        })
    return pd.DataFrame(summary)

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
