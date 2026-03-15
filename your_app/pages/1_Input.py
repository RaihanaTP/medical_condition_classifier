import streamlit as st
from bg import apply_bg
import numpy as np

apply_bg()

st.title("Patient Input")

with st.form("input_form"):

    st.subheader("Vitals and Core Metrics")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1.0, 120.0, 30.0, help="Your current age in years.")
        glucose = st.number_input("Glucose (mg/dL)", 50.0, 300.0, 90.0, help="Fasting blood glucose level. Normal range is typically below 100 mg/dL.")
        bmi = st.number_input("BMI (kg/m²)", 10.0, 60.0, 25.0, help="Body Mass Index, calculated from weight and height. Normal is 18.5 - 24.9.")
        chol = st.number_input("Total Cholesterol (mg/dL)", 100.0, 500.0, 200.0, help="Total cholesterol level. Ideal is typically below 200 mg/dL.")
        hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5, help="Average blood sugar level over the past 3 months. Normal is below 5.7%.")

    with col2:
        gender_str = st.selectbox("Gender", ["Male", "Female"], help="Biological sex for risk calculation.")
        gender = 0 if gender_str == "Male" else 1

        bp = st.number_input("Blood Pressure (mmHg)", 60.0, 200.0, 120.0, help="Systolic blood pressure. Normal is < 120.")
        oxy = st.number_input("Oxygen Saturation (%)", 70.0, 100.0, 98.0, help="Percentage of oxygen carried by the blood. Healthy range is 95% to 100%.")
        trig = st.number_input("Triglycerides (mg/dL)", 50.0, 600.0, 150.0, help="Fasting triglycerides level. Ideal is typically below 150 mg/dL.")

    st.subheader("Lifestyle and History")
    col3, col4 = st.columns(2)

    with col3:
        smoking_str = st.selectbox("Smoking", ["No", "Yes"], help="Do you currently smoke or have a history of smoking?")
        smoking = 1 if smoking_str == "Yes" else 0

        physical = st.number_input("Physical Activity (Score 0-10)", 0.0, 10.0, 5.0, help="How physically active are you? 0=Sedentary, 10=Highly Active.")
        family_str = st.selectbox("Family History of Condition", ["No", "Yes"], help="Do close family members have heart disease, diabetes, or cancer?")
        family = 1 if family_str == "Yes" else 0

    with col4:
        alcohol_str = st.selectbox("Alcohol Consumption", ["No", "Yes"], help="Do you consume alcohol regularly?")
        alcohol = 1 if alcohol_str == "Yes" else 0

        diet = st.number_input("Diet Score (0-10)", 0.0, 10.0, 5.0, help="Quality of your diet. 0=Very Poor, 10=Very Healthy.")
        stress = st.number_input("Stress Level (0-10)", 0.0, 10.0, 5.0, help="Perceived average stress level. 0=Relaxed, 10=Extremely Stressed.")
        sleep = st.number_input("Sleep Hours (h)", 0.0, 15.0, 7.0, help="Average hours of sleep per night. Recommended range is 7-9 hours.")

    st.markdown("---")
    submit = st.form_submit_button("✅ Predict")

if submit:
    input_vector = [
        age, gender, glucose, bp, bmi, oxy, chol, trig,
        hba1c, smoking, alcohol, physical, diet, family,
        stress, sleep
    ]
    st.session_state["input_data"] = np.array([input_vector])
    st.switch_page("pages/2_Result.py")