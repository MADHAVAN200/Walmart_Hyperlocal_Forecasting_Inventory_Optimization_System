import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Trend Analysis", layout="wide")
st.title("Social Trend Signal Analysis")
st.markdown("This module simulates trend data from social media and news signals to identify emerging product demands.")

# Step 1: Simulated Data

cities = ["Mumbai", "Delhi", "Chennai"]
products = ["Rice", "Milk", "Biscuits", "Shampoo", "Detergent"]

# Generate date range
today = datetime.today()
date_range = [today - timedelta(days=i) for i in range(14)][::-1]  # Last 14 days

# Simulated trend signal data
def simulate_trend_data():
    data = []
    np.random.seed(42)
    for city in cities:
        for product in products:
            base_score = np.random.randint(30, 80)
            trend_line = [base_score + np.random.randint(-10, 10) for _ in date_range]
            for date, score in zip(date_range, trend_line):
                data.append({
                    "City": city,
                    "Product": product,
                    "Date": date,
                    "Trend Score": max(0, score)
                })
    return pd.DataFrame(data)

df_trends = simulate_trend_data()

# Step 2: Filters

st.sidebar.subheader("Trend Filters")
selected_city = st.sidebar.selectbox("Select City", cities)
selected_product = st.sidebar.selectbox("Select Product", products)

df_filtered = df_trends[(df_trends["City"] == selected_city) & (df_trends["Product"] == selected_product)]

# Step 3: Line Chart

st.subheader(f"Trend Over Time - {selected_product} in {selected_city}")

fig = px.line(df_filtered,
              x="Date",
              y="Trend Score",
              title=f"Social Buzz Trend for {selected_product} in {selected_city}",
              markers=True)

fig.update_traces(line=dict(color='blue'))
fig.update_layout(xaxis_title="Date", yaxis_title="Trend Score (0-100)")
st.plotly_chart(fig, use_container_width=True)

# Step 4: Heatmap (Optional Overview)

st.subheader("City-Wise Product Buzz Heatmap")

df_latest = df_trends[df_trends["Date"] == df_trends["Date"].max()]
heatmap_data = df_latest.pivot(index="City", columns="Product", values="Trend Score")

st.dataframe(heatmap_data.style.background_gradient(cmap='Blues'), use_container_width=True)

# Step 5: Explanation

with st.expander("What is a Trend Score?"):
    st.markdown("""
    - The **Trend Score** is a simulated value that represents product buzz based on:
        - Twitter hashtags
        - Instagram mentions
        - News coverage
    """)

