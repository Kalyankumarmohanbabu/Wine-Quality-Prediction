import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and scaler
with open(r'D:\wine project\model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open(r'D:\wine project\scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit app
st.title('Wine Quality Prediction')

# Input features for a good wine example
fixed_acidity = st.slider('Fixed Acidity', 4.0, 16.0, 8.5)
volatile_acidity = st.slider('Volatile Acidity', 0.1, 1.5, 0.3)
citric_acid = st.slider('Citric Acid', 0.0, 1.0, 0.4)
residual_sugar = st.slider('Residual Sugar', 0.0, 15.0, 2.5)
chlorides = st.slider('Chlorides', 0.01, 0.2, 0.045)
free_sulfur_dioxide = st.slider('Free Sulfur Dioxide', 1.0, 72.0, 30.0)
total_sulfur_dioxide = st.slider('Total Sulfur Dioxide', 6.0, 289.0, 100.0)
density = st.slider('Density', 0.9900, 1.0050, 0.9950)
pH = st.slider('pH', 2.8, 4.0, 3.3)
sulphates = st.slider('Sulphates', 0.3, 2.0, 0.7)
alcohol = st.slider('Alcohol', 8.0, 15.0, 12.5)

# Create a dataframe for the input features
input_data = pd.DataFrame([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]], columns=['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol'])

# Scale the input features
input_data_scaled = scaler.transform(input_data)

# Predict the quality
if st.button('Predict Quality'):
    prediction = model.predict(input_data_scaled)
    quality = 'Good Wine' if prediction[0] == 1 else 'Bad Wine'
    st.write(f'The predicted quality of the wine is: {quality}')
