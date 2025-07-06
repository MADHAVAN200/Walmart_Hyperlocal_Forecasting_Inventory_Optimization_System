import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Federated Learning Panel", layout="wide")
st.title("Federated Learning Panel")
st.write("Monitor and control your edge AI model updates across stores using federated learning.")

# Simulate Store FL Status 
def generate_dummy_data():
    cities = ["Mumbai", "Delhi", "Chennai"]
    data = []
    for city in cities:
        last_updated = datetime.now() - timedelta(minutes=random.randint(1, 120))
        local_acc = round(random.uniform(85, 95), 2)
        global_gain = round(random.uniform(0.5, 2.5), 2)
        data.append({
            "Store": city,
            "Last Updated": last_updated.strftime("%Y-%m-%d %H:%M:%S"),
            "Local Model Accuracy (%)": local_acc,
            "Global Model Gain (%)": global_gain,
            "Status": random.choice(["Idle", "Training", "Ready for Update"])
        })
    return pd.DataFrame(data)

df = generate_dummy_data()

# ---- Display Table ----
st.subheader(" Store Edge AI Status")
st.dataframe(df, use_container_width=True)

# ---- Trigger Update Button ----
st.subheader("Trigger Federated Model Update")
if st.button("Run Federated Aggregation Now"):
    st.success("Federated update triggered successfully!")
    st.info("Model parameters from all stores will now be aggregated and synced.")

# ---- Help Section ----
with st.expander(" What is Federated Learning?"):
    st.write("""
    Federated Learning allows each Walmart store to train an AI model on its local data (sales, demand patterns) 
    without sending raw data to a central server. Only the trained parameters are shared. 
    This ensures privacy and allows for personalized, store-level models.
    
    After each store finishes training locally, the system combines updates into a global model,
    improving overall accuracy and adaptability.
    """)
