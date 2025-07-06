import streamlit as st

# App Configuration 
st.set_page_config(
    page_title="Walmart Unified Inventory & Forecasting",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App Title and Introduction 
st.title("Walmart Hyperlocal Forecasting & Inventory Optimization System")
st.markdown("---")

# Welcome Overview 
st.markdown("""
Welcome to the unified AI-powered dashboard built for **real-time inventory optimization** and **hyperlocal demand forecasting** using Edge AI, Federated Learning, and External Signals like Weather, Trends, and Events.

This system consists of the following modules, accessible from the sidebar:
""")

# Overview Table 
st.markdown("""
| Module | Description |
|--------|-------------|
|Trend Analysis | Simulated product demand signals from social media |
|Weather Tracker | Simulated weather patterns that influence demand |
|Event Calendar | Simulated events/festivals that impact stock movement |
|Forecast Engine | Combines all signals to predict product-level demand |
|FL Panel | Federated learning metrics across local stores |
|Inventory Dashboard | Visual insights into stock levels and alerts |
""")
