import streamlit as st
import requests

# Define the FastAPI endpoint
API_URL = "https://api-u65r.onrender.com/predict/"

st.title("Football Player Prediction")

# Input fields for the prediction
#position = st.number_input("Position", min_value=0, step=1)
age = st.number_input("Age", min_value=0, step=1)
appearances = st.number_input("Appearances", min_value=0, step=1)
goals = st.number_input("Goals", min_value=0, step=1)
# Add more input fields as needed

if st.button("Predict"):
    # Create the request payload
    payload = {
        #'Position': position,
        "age": age,
        "appearances": appearances,
        "goals": goals,
        # Add more fields as needed
    }
    
    # Make a POST request to the FastAPI service
    response = requests.post(API_URL, json=payload)
    prediction = response.json()
    
    # Display the prediction
    st.write(f"Predicted Category: {prediction['prediction']}")
