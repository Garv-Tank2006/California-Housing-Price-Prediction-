import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Real Estate AI", layout="wide")

st.title("🏡 California Housing Intelligence")

# --- SIDEBAR: USER INPUTS ---
with st.sidebar:
    st.header("Property Details")
    med_inc = st.number_input("Median Income (x$10k)", 0.5, 15.0, 3.5)
    house_age = st.slider("House Age (Years)", 1, 52, 25)
    ave_rooms = st.number_input("Average Rooms", 1.0, 10.0, 5.0)
    ave_bedrms = st.number_input("Average Bedrooms", 1.0, 5.0, 1.0)
    population = st.number_input("Area Population", 3, 35000, 1000)
    ave_occup = st.number_input("Avg Occupancy", 1.0, 6.0, 3.0)
    lat = st.number_input("Latitude", 32.0, 42.0, 34.2)
    lon = st.number_input("Longitude", -124.0, -114.0, -118.4)

# --- PAYLOAD CONSTRUCTION ---
payload = {
    "MedInc": med_inc,
    "HouseAge": house_age,
    "AveRooms": ave_rooms,
    "AveBedrms": ave_bedrms,
    "Population": population,
    "AveOccup": ave_occup,
    "Latitude": lat,
    "Longitude": lon
}

# --- API CALL ---
if st.button("Generate AI Prediction"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict_and_search", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            
            # Display Prediction
            st.metric("Predicted Market Value", f"${data['predicted_price']:,.2f}k")

            # Display Map & Data Table
            if "suggested_locations" in data:
                df = pd.DataFrame(data["suggested_locations"])
                
                # IMPORTANT: Rename columns for st.map compatibility
                map_df = df.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})
                
                c1, c2 = st.columns([1, 1])
                with c1:
                    st.subheader("📍 Recommended Areas")
                    st.map(map_df)
                with c2:
                    st.subheader("📋 Coordinates List")
                    st.dataframe(df, width="stretch")
        else:
            st.error("Backend Error: Check if main.py is running.")
            
    except Exception as e:
        st.error(f"Could not connect to API: {e}")