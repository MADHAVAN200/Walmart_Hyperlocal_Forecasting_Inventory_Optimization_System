import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

st.set_page_config(page_title="Event Calendar", layout="wide")
st.title("City Event Calendar")
st.write("Track upcoming festivals, sports, concerts, and major city events that can influence product demand.")

# ---- Step 1: Simulate or Load Event Data ----

# Simulated event data
event_data = pd.DataFrame({
    "Event Name": [
        "Ganesh Chaturthi", "Cricket World Cup Match", "Music Concert", "Diwali Festival", "Marathon Run", "Shopping Fest", "Food Carnival"
    ],
    "City": [
        "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai"
    ],
    "Date": [
        "2025-09-10", "2025-10-15", "2025-07-30", "2025-11-01", "2025-08-22", "2025-08-30", "2025-09-05"
    ],
    "Impact Score": [9.5, 8.7, 6.2, 10.0, 7.5, 6.9, 8.3]
})

# Convert to datetime
event_data["Date"] = pd.to_datetime(event_data["Date"])

# ---- Step 2: Filter Based on City or Date ----

city_filter = st.selectbox("📍 Select City", options=["All", "Mumbai", "Delhi", "Chennai"])

today = datetime.date.today()
future_events = event_data[event_data["Date"] >= pd.Timestamp(today)]

if city_filter != "All":
    filtered_events = future_events[future_events["City"] == city_filter]
else:
    filtered_events = future_events

# ---- Step 3: Display in Table ----

st.subheader("Upcoming Events")
st.dataframe(filtered_events.sort_values("Date"))

# ---- Step 4: Plot Demand Impact Timeline ----

st.subheader("Demand Impact by Event")
fig = px.scatter(
    filtered_events,
    x="Date",
    y="Impact Score",
    size="Impact Score",
    color="Event Name",
    hover_data=["City"],
    title="Demand Impact Timeline",
)

st.plotly_chart(fig, use_container_width=True)
