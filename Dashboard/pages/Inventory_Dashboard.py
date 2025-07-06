import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Inventory Dashboard", layout="wide")
st.title("Inventory Insights Dashboard")
st.markdown("Get a real-time overview of stock levels, demand forecasts, and alerts across stores.")


# Step 1: Simulated Inventory Data

cities = ["Mumbai", "Delhi", "Chennai"]
products = ["Rice", "Milk", "Biscuits", "Shampoo", "Detergent"]

def generate_inventory_data():
    data = []
    for city in cities:
        for product in products:
            current_stock = np.random.randint(50, 300)
            forecast_demand = np.random.randint(100, 250)
            shortage = forecast_demand > current_stock
            overstock = current_stock > forecast_demand * 1.5
            status = "Shortage" if shortage else "Overstock" if overstock else "Optimal"
            data.append({
                "Store": city,
                "Product": product,
                "Current Stock": current_stock,
                "Forecasted Demand": forecast_demand,
                "Status": status
            })
    return pd.DataFrame(data)

df_inventory = generate_inventory_data()

# Step 2: Filters

st.sidebar.subheader("Filters")
selected_city = st.sidebar.selectbox("Select Store", ["All"] + cities)
if selected_city != "All":
    df_inventory = df_inventory[df_inventory["Store"] == selected_city]

# Step 3: Display Table with Alerts

st.subheader("Inventory Summary")

def highlight_status(row):
    if row["Status"] == "Shortage":
        return ['background-color: #ffcccc; color: black; font-weight: bold'] * len(row)
    elif row["Status"] == "Overstock":
        return ['background-color: #fff3cd; color: black; font-weight: bold'] * len(row)
    elif row["Status"] == "Optimal":
        return ['background-color: #d4edda; color: black; font-weight: bold'] * len(row)
    else:
        return [''] * len(row)

st.dataframe(df_inventory.style.apply(highlight_status, axis=1), use_container_width=True)

# Step 4: Visualization

st.subheader("Product-wise Stock vs Demand")

selected_product = st.selectbox("Choose a product to visualize", products)

df_product = df_inventory[df_inventory["Product"] == selected_product]

fig = px.bar(df_product,
             x="Store",
             y=["Current Stock", "Forecasted Demand"],
             barmode="group",
             color_discrete_sequence=["#1f77b4", "#ff7f0e"],
             title=f"{selected_product} - Inventory vs Demand per Store")

st.plotly_chart(fig, use_container_width=True)

# Step 5: Summary KPIs

st.subheader("Overall Stock Health")

total_shortages = df_inventory[df_inventory["Status"] == "Shortage"].shape[0]
total_overstock = df_inventory[df_inventory["Status"] == "Overstock"].shape[0]
total_optimal = df_inventory[df_inventory["Status"] == "Optimal"].shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Shortages", total_shortages)
col2.metric("Overstocked", total_overstock)
col3.metric("Optimal Stock", total_optimal)

# Step 6: Explanation

with st.expander("How to use this dashboard"):
    st.markdown("""
    - This dashboard helps Walmart teams quickly identify inventory imbalances across stores.
    - Shortage: Stock is below forecasted demand → Replenishment needed.
    - Overstock: Stock is significantly higher than demand → May lead to wastage.
    - Optimal: Inventory is well balanced with demand.
    
    Use this tool to take action before stock-outs or overstocking affects performance.
    """)

