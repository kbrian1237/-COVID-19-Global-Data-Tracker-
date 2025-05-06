# This is a simple Streamlit app that visualizes COVID-19 data using a CSV file.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("owid-covid-data.csv")
df['date'] = pd.to_datetime(df['date'])

# Streamlit UI
st.title("COVID-19 Tracker Dashboard")

country = st.selectbox("Select a country", df['location'].unique())
date_range = st.date_input("Select date range", [df['date'].min(), df['date'].max()])

# Filter data
mask = (df['location'] == country) & (df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))
filtered = df[mask]

# Plot total cases
st.subheader(f"Total Cases in {country}")
fig, ax = plt.subplots()
ax.plot(filtered['date'], filtered['total_cases'], label='Total Cases')
ax.set_xlabel("Date")
ax.set_ylabel("Cases")
ax.grid(True)
st.pyplot(fig)
