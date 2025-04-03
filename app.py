
import streamlit as st
import pandas as pd
import plotly.express as px
from models import load_data

def main():
    st.title('Saudi Arabia Healthcare Statistics Dashboard')

    # Load data
    df = load_data()

    # Display data table
    st.subheader('Healthcare Statistics (2024)')
    st.table(df)

    # Create a bar chart for healthcare resource indicators
    st.subheader('Healthcare Resources per 10,000 Population')
    resources_df = df[df['Indicator'].str.contains('Beds|Physicians|Nurses')]
    fig = px.bar(resources_df, x='Indicator', y='Value', text='Value',
                 labels={'Value': 'Rate per 10,000 Population'})
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
