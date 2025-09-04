import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit app UI
st.title("🚗 Driver Rating Predictor")
st.write("Enter the details of the ride to predict the driver rating:")

# Input fields
distance = st.slider("Trip Distance (km)", 1.0, 30.0, 10.0)
duration = st.slider("Trip Duration (minutes)", 5, 60, 20)
time_of_day = st.selectbox("Time of Day", ['Morning', 'Afternoon', 'Evening', 'Night'])
traffic = st.selectbox("Traffic Level", ['Low', 'Medium', 'High'])
complaint = st.selectbox("Customer Complaint", ['No', 'Yes'])
trips_completed = st.slider("Trips Completed by Driver", 10, 500, 100)
avg_rating = st.slider("Driver's Avg Past Rating", 2.5, 5.0, 4.2)

# Encode inputs
time_of_day_map = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
traffic_map = {'Low': 1, 'Medium': 2, 'High': 0}
complaint_map = {'No': 0, 'Yes': 1}

input_data = pd.DataFrame({
    'Distance_km': [distance],
    'Duration_mins': [duration],
    'Time_of_Day': [time_of_day_map[time_of_day]],
    'Traffic': [traffic_map[traffic]],
    'Complaints': [complaint_map[complaint]],
    'Trips_Completed': [trips_completed],
    'Avg_Past_Rating': [avg_rating]
})

# Predict
if st.button("Predict Rating"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Driver Rating: ⭐ {round(prediction, 2)}")