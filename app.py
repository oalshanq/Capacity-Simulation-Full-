
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from models import simulate_demand, load_static_data

st.set_page_config(page_title="Saudi Healthcare Simulation", layout="wide")
st.title("Saudi Arabia Healthcare Simulation Dashboard")

# Sidebar inputs
regions = ["Riyadh", "Makkah", "Madinah", "Eastern Province", "Qassim", "Hail", 
           "Tabuk", "Jouf", "Nothern Borders", "Baha", "Assir", "Najran", "Jizan"]

specialties = ["Pediatrics", "General Surgery", "Internal Medicine", "Obstetrics", "Gynecology",
               "Cardiology", "Oncology", "Neurology", "Orthopedics", "Neurosurgery",
               "Cardiac Surgery", "Dentistry", "Dermatology", "Ophthalmology", "ENT",
               "Family Medicine", "Geriatrics", "Palliative Care"]

region = st.sidebar.selectbox("Select Region", regions)
specialty = st.sidebar.selectbox("Select Specialty", specialties)

if st.sidebar.button("Run Simulation"):
    df = simulate_demand(region, specialty)
    st.success(f"Simulation complete for {specialty} in {region}.")

    st.subheader("Projected Demand vs Capacity")
    fig = px.line(df, x="Year", y=["Demand", "Beds", "Physicians", "Nurses"], markers=True)
    st.plotly_chart(fig, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Results as CSV", csv, f"{region}_{specialty}_forecast.csv", "text/csv")

st.markdown("---")
st.header("National Healthcare Statistics (Static)")
st.dataframe(load_static_data())
