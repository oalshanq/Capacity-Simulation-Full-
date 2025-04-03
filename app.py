
import streamlit as st
import pandas as pd
import plotly.express as px
from models import simulate_demand_vbic, load_static_data

st.set_page_config(page_title="Saudi VBIC Healthcare Simulation", layout="wide")
st.title("Saudi Arabia Healthcare Forecast under Value-Based Integrated Care (VBIC)")

# Sidebar inputs
regions = ["Riyadh", "Makkah", "Madinah", "Eastern Province", "Qassim", "Hail", 
           "Tabuk", "Jouf", "Nothern Borders", "Baha", "Assir", "Najran", "Jizan"]

specialties = ["Pediatrics", "General Surgery", "Internal Medicine", "Obstetrics", "Gynecology",
               "Cardiology", "Oncology", "Neurology", "Orthopedics", "Neurosurgery",
               "Cardiac Surgery", "Dentistry", "Dermatology", "Ophthalmology", "ENT",
               "Family Medicine", "Geriatrics", "Palliative Care"]

region = st.sidebar.selectbox("Select Region", regions)
specialty = st.sidebar.selectbox("Select Specialty", specialties)

if st.sidebar.button("Run VBIC Simulation"):
    df = simulate_demand_vbic(region, specialty)
    st.success(f"VBIC Forecast complete for {specialty} in {region}.")

    st.subheader("Forecasted Resource Demand per 1,000 Population")
    fig = px.line(df, x="Year", y=["Beds_per_1k", "Nurses_per_1k", "Outpatient_Clinics_per_1k", "Physician_Clinics_per_1k"],
                  markers=True, labels={
                      "Beds_per_1k": "Beds",
                      "Nurses_per_1k": "Nurses",
                      "Outpatient_Clinics_per_1k": "Outpatient Clinics",
                      "Physician_Clinics_per_1k": "Physician Clinics"
                  })
    st.plotly_chart(fig, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, f"{region}_{specialty}_vbic_forecast.csv", "text/csv")

st.markdown("---")
st.header("National Healthcare Statistics (Static)")
st.dataframe(load_static_data())
