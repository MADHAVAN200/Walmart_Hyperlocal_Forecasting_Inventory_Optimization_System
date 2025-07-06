import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Forecast Engine", layout="wide")
st.title("AI Forecast Engine")
st.write("Predict demand trends by combining weather, event, and trend signals.")

# STEP 1: Simulate Input Data

city = st.selectbox("Select Store Location", ["Mumbai", "Delhi", "Chennai"])
base_date = datetime.today()

# Simulated past sales data
days = 30
future_days = 7
np.random.seed(42)
past_sales = np.random.poisson(lam=200, size=days)

# Simulate signal boosts (e.g., event or weather)
event_boost = {"Mumbai": 1.3, "Delhi": 1.2, "Chennai": 1.1}
weather_factor = {"Mumbai": 1.1, "Delhi": 1.0, "Chennai": 1.2}
social_trend = {"Mumbai": 1.2, "Delhi": 1.1, "Chennai": 1.05}

# STEP 2: Predict Future Demand

# Get boost multiplier
boost = event_boost[city] * weather_factor[city] * social_trend[city]

# Use a simple trend-based forecast
last_known = past_sales[-1]
forecast = [int(last_known * boost * np.random.uniform(0.95, 1.1)) for _ in range(future_days)]

# STEP 3: Create DataFrame for Plotting

dates = [base_date - timedelta(days=i) for i in range(days)][::-1]
future_dates = [base_date + timedelta(days=i + 1) for i in range(future_days)]

df_past = pd.DataFrame({"Date": dates, "Sales": past_sales})
df_future = pd.DataFrame({"Date": future_dates, "Sales": forecast})
# STEP 4: Plotting

fig = go.Figure()

fig.add_trace(go.Scatter(x=df_past["Date"], y=df_past["Sales"],
                         mode='lines+markers', name="Past Sales", line=dict(color='blue')))

fig.add_trace(go.Scatter(x=df_future["Date"], y=df_future["Sales"],
                         mode='lines+markers', name="Forecast", line=dict(color='orange', dash='dash')))

fig.update_layout(
    title=f"Demand Forecast for {city}",
    xaxis_title="Date",
    yaxis_title="Units Sold",
    legend_title="Data Type",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# STEP 5: Display Table

st.subheader("Forecast Summary")
st.dataframe(df_future.set_index("Date"), use_container_width=True)

# STEP 6: Explanation

with st.expander("How this forecast works"):
    st.markdown("""
    This prototype simulates a demand forecasting engine that factors in:
    
    - Trend signals from social media
    - Local event boosts based on city
    - Weather data from API
    
    The boost is multiplied with recent sales history to simulate future demand.""")
