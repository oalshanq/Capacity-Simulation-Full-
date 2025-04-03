
import streamlit as st
import pandas as pd
import plotly.express as px
from models import simulate_with_real_supply, load_real_supply_data

st.set_page_config(page_title="Saudi Healthcare Simulation (Real Data)", layout="wide")
st.title("Saudi Arabia Healthcare Simulation Dashboard (Real Supply Data)")

df_supply = load_real_supply_data()
regions = df_supply["Region"].tolist()

specialties = ["Pediatrics", "General Surgery", "Internal Medicine", "Obstetrics", "Gynecology",
               "Cardiology", "Oncology", "Neurology", "Orthopedics", "Neurosurgery",
               "Cardiac Surgery", "Dentistry", "Dermatology", "Ophthalmology", "ENT",
               "Family Medicine", "Geriatrics", "Palliative Care"]

region = st.sidebar.selectbox("Select Region", regions)
specialty = st.sidebar.selectbox("Select Specialty", specialties)

if st.sidebar.button("Run Simulation"):
    df = simulate_with_real_supply(region, specialty, df_supply)
    st.success(f"Simulation for {specialty} in {region} completed.")

    st.subheader("Forecasted Demand vs Real Supply (per 1,000 population)")
    fig = px.line(df, x="Year", y=[
        "Beds_Demand", "Beds_Supply",
        "Nurses_Demand", "Nurses_Supply",
        "Clinics_Demand", "Clinics_Supply",
        "Physicians_Demand", "Physicians_Supply"
    ])
    st.plotly_chart(fig, use_container_width=True)

    st.download_button("Download Forecast as CSV", df.to_csv(index=False).encode("utf-8"),
                       file_name=f"{region}_{specialty}_forecast.csv")
