import streamlit as st
import requests

st.title("Football Player Prediction")

# Collect user input
age = st.number_input("Age", min_value=0)
appearances = st.number_input("Appearances", min_value=0)
goals = st.number_input("Goals", min_value=0)

position = st.text_input("Enter Position", "")


# Button to submit data
if st.button("Predict"):
    player_data = {
        "age": age,
        "appearances": appearances,
        "goals": goals,
        "position": position
    }
    # Send data to FastAPI
    response = requests.post("https://api-u65r.onrender.com/predict", json=player_data)
    prediction = response.json()["prediction"]
    
    st.write(f"Prediction: {prediction}")
