# BigRetailers Forecasting & Inventory Optimization System
This project is a prototype for real-time inventory optimization and demand forecasting at the store level using AI techniques including Federated Learning, Edge Computing, and external signals like social trends, weather, and local events.

## Key Modules
- **Trend Signal Module**: Extracts or simulates social demand trends.
- **Weather Tracker**: Simulates local weather forecasts per store.
- **Event Calendar**: Simulates local events/festivals impacting demand.
- **Forecast Engine**: Predicts product-level demand using AI.
- **Edge Model Trainer**: Trains local models at each store (client).
- **Federated Aggregator**: Combines updates from multiple clients securely.
- **Inventory Dashboard**: Visualizes stock levels, demand forecasts, and alerts.

## Tech Stack
- Python, Streamlit
- PyTorch, NumPy, Pandas
- Flower (for Federated Learning)
- Plotly (for visualizations)

## How to Run
1. Clone this repo  
   `git clone https://github.com/your-username/Walmart-Hyperlocal-Forecasting-Inventory-Optimization-System.git`
2. Set up a Python virtual environment and install dependencies  
   `pip install -r requirements.txt`
3. Run Federated Server  
   `python fl_server.py`
4. Run clients in separate terminals  
   `python client_mumbai.py`, `python client_delhi.py`, etc.
5. Start the dashboard  
   ```bash
   cd dashboard
   streamlit run app.py

Note:
Dummy data is used for simulation. No paid APIs required.
This is a prototype. For production, integrate with secure cloud infrastructure and APIs.

