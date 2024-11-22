
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
loaded_model = joblib.load('final_model.joblib')

# Function to make predictions
def predict_asthma(input_data):
    input_df = pd.DataFrame(input_data)
    prediction = loaded_model.predict(input_df)
    return prediction

# Streamlit app
st.title("Asthma Detection")

# Introduction About Asthma
st.markdown("""
Asthma is a chronic condition that affects the airways in your lungs. It causes recurring periods of wheezing, chest tightness, shortness of breath, and coughing. Asthma symptoms can range from mild to severe and can be triggered by various factors, including allergens, exercise, cold air, and respiratory infections.
""")

# Picture Header
st.image("asthma.png", use_container_width=True)

# Input Options Section
st.header("Input Options")

# Symptom inputs
symptoms = {
    "Tiredness": st.checkbox("Tiredness"),
    "Dry-Cough": st.checkbox("Dry-Cough"),
    "Difficulty-in-Breathing": st.checkbox("Difficulty-in-Breathing"),
    "Sore-Throat": st.checkbox("Sore-Throat"),
    "Pains": st.checkbox("Pains"),
    "Nasal-Congestion": st.checkbox("Nasal-Congestion"),
    "Runny-Nose": st.checkbox("Runny-Nose"),
}

# Age input
age_options = ["Age_0-9", "Age_10-19", "Age_20-24", "Age_25-59", "Age_60+"]
selected_age = st.radio("Age Group", age_options)

# Gender input
gender_options = ["Female", "Male"]
selected_gender = st.radio("Gender", gender_options)

# Encoding the inputs for the model
age_encoding = [1 if selected_age == age_option else 0 for age_option in age_options]
gender_encoding = [1 if selected_gender == gender_option else 0 for gender_option in gender_options]

# Creating the input data dictionary
data = {
    'Tiredness': [symptoms["Tiredness"]],
    'Dry-Cough': [symptoms["Dry-Cough"]],
    'Difficulty-in-Breathing': [symptoms["Difficulty-in-Breathing"]],
    'Sore-Throat': [symptoms["Sore-Throat"]],
    'Pains': [symptoms["Pains"]],
    'Nasal-Congestion': [symptoms["Nasal-Congestion"]],
    'Runny-Nose': [symptoms["Runny-Nose"]],
    'Age_0-9': age_encoding[0],
    'Age_10-19': age_encoding[1],
    'Age_20-24': age_encoding[2],
    'Age_25-59': age_encoding[3],
    'Age_60+': age_encoding[4],
    'Gender_Female': gender_encoding[0],
    'Gender_Male': gender_encoding[1]
}

# Predict button
if st.button("Predict"):
    prediction = predict_asthma(data)
    result = 'Asthma' if prediction[0] == 0 else 'Not Asthma'
    if result == 'Asthma':
        st.write(f"<p style='font-size: 24px; color: red;'>Prediction: {result}</p>", unsafe_allow_html=True)
    else:
        st.write(f"<p style='font-size: 24px; color: green;'>Prediction: {result}</p>", unsafe_allow_html=True)



