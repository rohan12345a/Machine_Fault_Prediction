# Failure Probability Prediction using Machine Learning and IoT Data

This project aims to predict the failure probability of industrial equipment using Machine Learning (ML) algorithms. The data is manually synthetized, preprocessed, and visualized using Power BI, with the final model deployed in a Streamlit application for real-time predictions.

## Overview

In this project, we used **IoT (Internet of Things)** data collected from various sensors on equipment to predict potential failures. The data includes features such as equipment type, operating temperature, pressure, flow rate, and vibration levels. Machine Learning models, specifically XGBoost, were applied to this data to predict the failure probability.

Additionally, a Power BI dashboard was created to visualize equipment health and performance metrics, and a Streamlit application was developed for real-time prediction.
## User Interaction UI


https://github.com/user-attachments/assets/0d50cc82-ed42-4002-9d66-368645f48bf5


## Key Steps

1. **Data Creation and Preprocessing**:  
   - Synthetic data was created to simulate sensor readings and equipment performance.
   - The data was preprocessed by encoding categorical variables and scaling continuous variables using a `StandardScaler`.

2. **Model Training**:  
   - An XGBoost regression model was used to predict the failure probability based on the preprocessed data.
   - The model was saved using `joblib` for later use in the Streamlit application.

3. **Deployment in Streamlit**:  
   - The Streamlit app allows users to input equipment data and get predictions on the failure probability.
   - The app uses the trained XGBoost model and standard scaler to process input and generate predictions.

4. **Visualization with Power BI**:  
   - A Power BI dashboard was created to monitor and visualize equipment health status, predicted failure probabilities, and other key performance indicators.

## Features

- **Real-Time Prediction**: Users can enter operational parameters of equipment (e.g., temperature, pressure, vibration) and get the predicted failure probability.
- **Interactive Dashboard**: The Power BI dashboard provides insights into the overall health and performance of equipment based on the predictive model.
- **IoT Integration**: The project simulates the real-time data collection process from IoT-enabled equipment.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-name.git
