import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Weather Tracker", layout="wide")
st.title("Weather Tracker")
st.markdown("Understand how weather patterns may impact product demand across different Walmart locations.")

# Step 1: Define Cities and Weather Conditions

cities = ["Mumbai", "Delhi", "Chennai"]
conditions = ["Sunny", "Rainy", "Cloudy", "Stormy", "Humid"]

# Step 2: Simulate Weather Forecast

def generate_weather_data():
    data = []
    for city in cities:
        for i in range(7):  # Forecast for next 7 days
            date = datetime.today() + timedelta(days=i)
            temperature = np.random.randint(25, 40)
            humidity = np.random.randint(40, 90)
            condition = np.random.choice(conditions, p=[0.4, 0.3, 0.2, 0.05, 0.05])
            data.append({
                "City": city,
                "Date": date.date(),
                "Condition": condition,
                "Temperature (°C)": temperature,
                "Humidity (%)": humidity
            })
    return pd.DataFrame(data)

df_weather = generate_weather_data()

# Step 3: User Filters

st.sidebar.subheader("Select Store City")
selected_city = st.sidebar.selectbox("City", cities)

df_filtered = df_weather[df_weather["City"] == selected_city]

# Step 4: Display Forecast Table

st.subheader(f"7-Day Weather Forecast for {selected_city}")
st.dataframe(df_filtered.set_index("Date"), use_container_width=True)

# Step 5: Visualize Temperature and Humidity

st.subheader("Temperature & Humidity Trends")

fig = px.line(df_filtered, x="Date", y=["Temperature (°C)", "Humidity (%)"],
              markers=True, title="Weather Impact Trends",
              labels={"value": "Metric", "variable": "Weather Feature"},
              color_discrete_map={"Temperature (°C)": "#FF5733", "Humidity (%)": "#3498db"})

st.plotly_chart(fig, use_container_width=True)

# Step 6: Explanation

with st.expander("Why track weather?"):
    st.markdown("""
    - Weather impacts product demand significantly:
        - Rain increases demand for umbrellas, instant food, medicine
        - Heat increases demand for beverages, ACs, skincare
        - Cold drives demand for blankets, heaters, soups
    - This simulated module forecasts temperature and humidity trends that can be used to adjust stock and trigger alerts.
    """)
