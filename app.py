
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from models import run_simulation, get_region_coords

st.set_page_config(page_title="Saudi Healthcare Simulation Dashboard", layout="wide")
st.title("Saudi Arabia Healthcare Forecasting Dashboard with Maps")

regions = [
    "Riyadh", "Makkah", "Madinah", "Eastern Province", "Qassim", "Hail", "Tabuk",
    "Jouf", "Nothern Borders", "Baha", "Assir", "Najran", "Jizan"
]

specialties = [
    "Pediatrics", "General Surgery", "Internal Medicine", "Obstetrics", "Gynecology",
    "Cardiology", "Oncology", "Neurology", "Orthopedics", "Neurosurgery",
    "Cardiac Surgery", "Dentistry", "Dermatology", "Ophthalmology", "ENT",
    "Family Medicine", "Geriatrics", "Palliative Care"
]

region = st.sidebar.selectbox("Select Region", regions)
specialty = st.sidebar.selectbox("Select Specialty", specialties)

if "results" not in st.session_state:
    st.session_state["results"] = None

if st.sidebar.button("Run Simulation"):
    st.session_state["results"] = run_simulation(region=region, specialty=specialty)

if st.session_state["results"] is not None:
    df = st.session_state["results"]

    st.subheader(f"Forecast for {specialty} in {region}")
    st.markdown("**Demand = projected number of patients requiring this specialty's services per year.**")
    fig = px.line(df, x="Year", y=["Demand", "Beds", "Physicians", "Nurses"], markers=True)
    fig.update_yaxes(title="Resource Quantity")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Map of Regions")
    coords = get_region_coords()
    fmap = folium.Map(location=[23.8859, 45.0792], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(fmap)
    for reg, coord in coords.items():
        folium.Marker(location=coord, popup=reg, tooltip=reg,
                      icon=folium.Icon(color="blue")).add_to(marker_cluster)
    st_folium(fmap, width=700)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, file_name=f"{region}_{specialty}_forecast.csv", mime="text/csv")
else:
    st.info("Click 'Run Simulation' to generate forecast and view maps.")
