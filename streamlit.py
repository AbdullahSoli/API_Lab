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

    try:
        # Send data to FastAPI
        response = requests.post("https://api-u65r.onrender.com", json=player_data)
        response.raise_for_status()  # Will raise an HTTPError for bad responses

        # Extract and display prediction
        prediction = response.json().get("prediction", "No prediction found")
        st.write(f"Prediction: {prediction}")
        
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
