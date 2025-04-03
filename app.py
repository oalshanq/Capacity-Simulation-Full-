
import streamlit as st
import pandas as pd
import plotly.express as px
from models import simulate_demand_supply_vbic, load_static_data, all_regions_forecast, specialty_summary

st.set_page_config(page_title="Saudi VBIC Healthcare Simulation", layout="wide")
st.title("Saudi Arabia VBIC Healthcare Simulation Dashboard")

regions = ["Riyadh", "Makkah", "Madinah", "Eastern Province", "Qassim", "Hail", 
           "Tabuk", "Jouf", "Nothern Borders", "Baha", "Assir", "Najran", "Jizan"]

specialties = ["Pediatrics", "General Surgery", "Internal Medicine", "Obstetrics", "Gynecology",
               "Cardiology", "Oncology", "Neurology", "Orthopedics", "Neurosurgery",
               "Cardiac Surgery", "Dentistry", "Dermatology", "Ophthalmology", "ENT",
               "Family Medicine", "Geriatrics", "Palliative Care"]

region = st.sidebar.selectbox("Select Region", regions)
specialty = st.sidebar.selectbox("Select Specialty", specialties)

if st.sidebar.button("Run Forecast"):
    df = simulate_demand_supply_vbic(region, specialty)
    st.success(f"Forecast complete for {specialty} in {region}.")
    st.subheader("Forecasted Resource Demand vs Status Quo Supply (per 1,000 population)")
    fig = px.line(df, x="Year", y=[
        "Beds_Demand", "Beds_Supply",
        "Nurses_Demand", "Nurses_Supply",
        "Outpatient_Clinics_Demand", "Outpatient_Clinics_Supply",
        "Physicians_Demand", "Physicians_Supply"
    ])
    st.plotly_chart(fig, use_container_width=True)
    st.download_button("Download Forecast CSV", df.to_csv(index=False).encode("utf-8"),
                       file_name=f"{region}_{specialty}_vbic_demand_supply.csv")

st.markdown("---")
st.header("Healthcare Resource Gaps Across Regions (Heatmap)")
heat_df = all_regions_forecast(specialties)
st.dataframe(heat_df)
fig_heat = px.imshow(heat_df.set_index("Region"),
                     labels=dict(color="Gap Index"),
                     color_continuous_scale="RdBu_r",
                     title="Demand-Supply Gap Index by Specialty and Region")
st.plotly_chart(fig_heat)

st.markdown("---")
st.header("Specialty Summary Across All Regions")
summary_df = specialty_summary(specialties, regions)
st.dataframe(summary_df)
fig_summary = px.bar(summary_df, x="Specialty", y=["Beds_Gap", "Nurses_Gap", "Clinics_Gap", "Physicians_Gap"],
                     barmode="group", title="Average Demand-Supply Gap by Specialty")
st.plotly_chart(fig_summary)

st.markdown("---")
st.subheader("National Healthcare Statistics (Static)")
st.dataframe(load_static_data())
