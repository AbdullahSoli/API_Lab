import streamlit as st
import requests

st.title("Football Player Prediction")

# Collect user input
age = st.number_input("Age", min_value=0)
appearances = st.number_input("Appearances", min_value=0)
goals = st.number_input("Goals", min_value=0)

# Add input fields for other features...
# Example: position_attack_centre_forward
positions = [
    "Attack Centre-Forward",
    "Attack LeftWinger",
    "Attack RightWinger",
    "Attack Second Striker",
    "Defender Centre-Back",
    "Defender Left-Back",
    "Defender Right-Back",
    "Goalkeeper",
    "Midfield Attacking Midfield",
    "Midfield Central Midfield",
    "Midfield Defensive Midfield",
    "Midfield Left Midfield",
    "Midfield Right Midfield"
]
position = st.selectbox("Position", positions)

# Button to submit data
if st.button("Predict"):
    player_data = {
        "age": age,
        "appearances": appearances,
        "goals": goals,
        "position": position
    }
    # Send data to FastAPI
    response = requests.post("https://your-render-url.com/predict/", json=player_data)
    prediction = response.json()["prediction"]
    
    st.write(f"Prediction: {prediction}")
