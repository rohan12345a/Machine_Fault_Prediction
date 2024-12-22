import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the XGBoost model
model = joblib.load("C:\\Users\\Lenovo\\Downloads\\xgb_regressor_model.joblib")

# Load StandardScaler used during model training
scaler = joblib.load("C:\\Users\\Lenovo\\Downloads\\scaler.joblib")  # Assuming you saved the scaler


# Function to preprocess the input data (same as in the training process)
def preprocess_input(data):
    # Manually encoding categorical features based on the unique values you provided
    equipment_type_mapping = {'Type1': 0, 'Type2': 1, 'Type3': 2, 'Type4': 3}
    location_mapping = {'Location1': 0, 'Location2': 1, 'Location3': 2, 'Location4': 3}
    fault_type_mapping = {'Type1': 1, 'Type2': 0, 'Type3': 4, 'Type4': 5, 'Type5': 2, 'Type6': 3}
    failure_mode_mapping = {'Prediction1': 3, 'Prediction2': 2, 'Prediction3': 1, 'Prediction4': 4}
    air_quality_mapping = {'Good': 0, 'Fair': 1, 'Poor': 2}

    # Apply the encoding based on mappings
    data['Equipment Type'] = data['Equipment Type'].map(equipment_type_mapping)
    data['Location'] = data['Location'].map(location_mapping)
    data['Fault Type'] = data['Fault Type'].map(fault_type_mapping)
    data['Failure Mode Prediction'] = data['Failure Mode Prediction'].map(failure_mode_mapping)
    data['Air Quality'] = data['Air Quality'].map(air_quality_mapping)

    # Standardize the features
    data_scaled = scaler.transform(data)
    return data_scaled


# Streamlit UI
st.title("Failure Probability Prediction")

# Display information about Condition Monitoring of Machines
st.subheader("What is Condition Monitoring of Machines?")
st.write("""
Condition Monitoring (CM) of machines refers to the practice of monitoring the health and performance of industrial equipment through various indicators. 
This includes measurements like vibration, temperature, pressure, and power consumption. Monitoring these parameters helps detect early signs of equipment failure, 
allowing maintenance to be performed before a catastrophic breakdown occurs. 
Condition monitoring is crucial for ensuring the operational efficiency, safety, and reliability of machines, while minimizing downtime and reducing repair costs.
""")


st.subheader("How Condition Monitoring Can Be Solved Using IoT and ML")
st.write("""
Condition monitoring can be enhanced by integrating **IoT (Internet of Things)** devices to collect real-time data from equipment sensors. These IoT-enabled sensors can continuously measure parameters such as temperature, vibration, pressure, and others, transmitting this data to a centralized platform.

Machine Learning (ML) algorithms can then be applied to analyze this data. By processing historical data and recognizing patterns associated with failures, ML models can predict when equipment is likely to fail. This allows for **predictive maintenance**, where maintenance is performed just before a failure occurs, rather than on a set schedule or after a failure happens.

### Key Advantages of Using IoT and ML for Condition Monitoring:
1. **Real-Time Data Collection**: IoT devices enable the continuous monitoring of machine conditions, providing real-time data for analysis.
2. **Early Failure Detection**: ML models can predict failures by learning from patterns in sensor data, allowing maintenance teams to act before the equipment breaks down.
3. **Optimization of Maintenance Schedules**: By predicting when maintenance is required, IoT and ML can help optimize schedules, minimizing downtime and reducing maintenance costs.
4. **Improved Decision Making**: With real-time insights and predictive analytics, organizations can make more informed decisions regarding equipment management and maintenance strategies.

In this application, we predict the failure probability of equipment based on various operational parameters, using machine learning algorithms and data inputs gathered from IoT devices.
""")

st.write("Enter the details below to predict the failure probability of equipment.")


# User input form
equipment_type = st.selectbox('Equipment Type', ['Type1', 'Type2', 'Type3', 'Type4'])
location = st.selectbox('Location', ['Location1', 'Location2', 'Location3', 'Location4'])
operating_temperature = st.number_input('Operating Temperature (°C)', value=25)
operating_pressure = st.number_input('Operating Pressure (bar)', value=5)
flow_rate = st.number_input('Flow Rate (m3/h)', value=100.0)
power_consumption = st.number_input('Power Consumption (kW)', value=50)
speed_rpm = st.number_input('Speed (RPM)', value=1500)
vibration_level = st.number_input('Vibration Level (mm/s)', value=0.5)
health_status = st.selectbox('Health Status', [2, 0, 1])
fault_type = st.selectbox('Fault Type', ['Type1', 'Type2', 'Type3', 'Type4', 'Type5', 'Type6'])
wear_and_tear = st.number_input('Wear & Tear (%)', value=10)
maintenance_interval = st.number_input('Maintenance Interval (days)', value=30)
time_since_last_maintenance = st.number_input('Time Since Last Maintenance (days)', value=5)
failure_mode_prediction = st.selectbox('Failure Mode Prediction', ['Prediction1', 'Prediction2', 'Prediction3', 'Prediction4'])
ambient_temperature = st.number_input('Ambient Temperature (°C)', value=20)
humidity = st.number_input('Humidity (%)', value=60)
air_quality = st.selectbox('Air Quality', [0, 2, 1])

# Collecting the input data into a DataFrame
input_data = pd.DataFrame({
    'Equipment Type': [equipment_type],
    'Location': [location],
    'Operating Temperature (°C)': [operating_temperature],
    'Operating Pressure (bar)': [operating_pressure],
    'Flow Rate (m3/h)': [flow_rate],
    'Power Consumption (kW)': [power_consumption],
    'Speed (RPM)': [speed_rpm],
    'Vibration Level (mm/s)': [vibration_level],
    'Health Status': [health_status],
    'Fault Type': [fault_type],
    'Wear & Tear (%)': [wear_and_tear],
    'Maintenance Interval (days)': [maintenance_interval],
    'Time Since Last Maintenance (days)': [time_since_last_maintenance],
    'Failure Mode Prediction': [failure_mode_prediction],
    'Ambient Temperature (°C)': [ambient_temperature],
    'Humidity (%)': [humidity],
    'Air Quality': [air_quality]
})

# Button to trigger prediction
if st.button('Predict Failure Probability'):
    # Preprocess the input data and make the prediction
    preprocessed_data = preprocess_input(input_data)
    prediction = model.predict(preprocessed_data)

    # Show the result
    st.write(f"The predicted failure probability is: {prediction[0]:.2f}%")

# Author info
with st.container():
    with st.sidebar:
        members = [
            {"name": "Rohan Saraswat", "email": "rohan.saraswat2003@gmail.com", "linkedin": "https://www.linkedin.com/in/rohan-saraswat-a70a2b225/"},
        ]

        # Define the page title and heading
        st.markdown("<h1 style='font-size:28px'>Author</h1>", unsafe_allow_html=True)

        # Iterate over the list of members and display their details
        for member in members:
            st.write(f"Name: {member['name']}")
            st.write(f"Email: {member['email']}")
            st.write(f"LinkedIn: {member['linkedin']}")
            st.write("")
