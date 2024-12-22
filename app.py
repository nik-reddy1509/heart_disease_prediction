import streamlit as st
import requests

# Streamlit app title and description
st.title("Heart Disease Prediction App")
st.write("This app interacts with a FastAPI model to predict the likelihood of heart disease.")

# Input fields for user input
st.sidebar.header("Input Features")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=45)
bp = st.sidebar.number_input("Blood Pressure (BP)", min_value=50, max_value=200, value=120)
cholesterol = st.sidebar.number_input("Cholesterol", min_value=100, max_value=400, value=200)
max_hr = st.sidebar.number_input("Maximum Heart Rate", min_value=50, max_value=220, value=150)
st_depression = st.sidebar.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.5, step=0.1)
chest_pain_type = st.sidebar.selectbox("Chest Pain Type", options=[1, 2, 3, 4], index=0)
thallium = st.sidebar.selectbox("Thallium Test Result", options=[3, 6, 7], index=0)

# Prediction button
if st.sidebar.button("Predict"):
    # FastAPI endpoint URL
    api_url = "http://<your-fastapi-deployment-url>/predict"  # Replace with your FastAPI URL

    # Input data for the FastAPI
    input_data = {
        "Age": age,
        "BP": bp,
        "Cholesterol": cholesterol,
        "Max_HR": max_hr,
        "ST_depression": st_depression,
        "Chest_pain_type": chest_pain_type,
        "Thallium": thallium
    }

    try:
        # Send POST request to the FastAPI app
        response = requests.post(api_url, json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            # Display results
            st.success(f"Prediction: {'Presence' if prediction == 1 else 'Absence'} of Heart Disease")
            st.write(f"Probability: {probability}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
