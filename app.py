import streamlit as st
import requests

st.title("California House Price Prediction")
st.sidebar.header("Input Features")

# Sidebar inputs
med_inc = st.sidebar.number_input("Median Income", value=3.5)
house_age = st.sidebar.number_input("House Age", value=20.0)
ave_rooms = st.sidebar.number_input("Average Rooms", value=5.0)
ave_bedrms = st.sidebar.number_input("Average Bedrooms", value=1.0)
population = st.sidebar.number_input("Population", value=1000.0)
ave_occup = st.sidebar.number_input("Average Occupancy", value=3.0)
latitude = st.sidebar.number_input("Latitude", value=34.0)
longitude = st.sidebar.number_input("Longitude", value=-118.0)

if st.button("Get Prediction"):
    # FIX 1: Capitalize keys to match FastAPI/Model
    input_data = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        
        if response.status_code == 200:
            # FIX 2: Match the key returned by the API
            prediction = response.json()['Predicted_Price']

            st.success(f"The Predicted House Price is: ${prediction*100000:,.2f}")

            avg_price = 2.06
            col1, col2 = st.columns(2)
            
            # FIX 3: Fixed the format string (changed :,0.f to :,.0f)
            col1.metric("Your Prediction", f"${prediction*100:,.0f}k")
            col2.metric("Average Price", f"${avg_price*100:,.0f}k")
        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"Could not connect to API: {e}")