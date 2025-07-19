import streamlit as st
import joblib as jl
import numpy as np

st.title("Salary Prediction App")
st.divider()
st.write("This app predicts the salary based on years of experience.")
# Load the pre-trained model
model = jl.load('salary_prediction_model.pkl')


# Input from the user
years_of_experience = st.number_input("Enter years of experience:",value=1, min_value=0, max_value=50, step=1)
job_rate = st.slider(value=3.5,step=0.1,min_value=0.0,max_value=5.0,label="Job Rate (0-5)")

x=[years_of_experience, job_rate]
st.divider()
pridicts=st.button("Predict Salary")
st.divider()
# Predict the salary
predicted_salary = model.predict(np.array([x]))[0]
# Display the result
if pridicts:
      st.balloons()
      st.write(f"Predicted Salary: {predicted_salary}")
else:
      st.write("Click the button to predict the salary.")

# To run the app, use the command: streamlit run app.py