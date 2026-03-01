# import streamlit as st
# from bg import apply_bg
#
# apply_bg()
#
#
# import numpy as np
#
#
# st.title(" Patient Input")
#
# with st.form("input_form"):
#
#     age = st.number_input("Age", 1.0, 120.0, 30.0)
#     gender = st.selectbox("Gender", ["Male", "Female"])
#     gender = 0 if gender == "Male" else 1
#
#     glucose = st.number_input("Glucose", 50.0, 300.0, 90.0)
#     bp = st.number_input("Blood Pressure", 60.0, 200.0, 120.0)
#     bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
#     oxy = st.number_input("Oxygen Saturation", 70.0, 100.0, 98.0)
#     chol = st.number_input("Cholesterol", 100.0, 500.0, 200.0)
#     trig = st.number_input("Triglycerides", 50.0, 600.0, 150.0)
#     hba1c = st.number_input("HbA1c", 3.0, 15.0, 5.5)
#
#     smoking = st.selectbox("Smoking", ["No", "Yes"])
#     smoking = 1 if smoking == "Yes" else 0
#
#     alcohol = st.selectbox("Alcohol", ["No", "Yes"])
#     alcohol = 1 if alcohol == "Yes" else 0
#
#     physical = st.number_input("Physical Activity", 0.0, 10.0, 5.0)
#     diet = st.number_input("Diet Score", 0.0, 10.0, 5.0)
#
#     family = st.selectbox("Family History", ["No", "Yes"])
#     family = 1 if family == "Yes" else 0
#
#     stress = st.number_input("Stress Level", 0.0, 10.0, 5.0)
#     sleep = st.number_input("Sleep Hours", 0.0, 15.0, 7.0)
#
#     submit = st.form_submit_button("✅ Predict")
#
# if submit:
#     st.session_state["input_data"] = np.array([[
#         age, gender, glucose, bp, bmi, oxy, chol, trig,
#         hba1c, smoking, alcohol, physical, diet, family,
#         stress, sleep
#     ]])
#
#     st.switch_page("pages/2_Result.py")
#
import streamlit as st
from bg import apply_bg
import numpy as np

# Apply background styling
apply_bg()

st.title("Patient Input")

with st.form("input_form"):

    # --- Section 1: Vitals & Core Metrics (2 columns per row) ---

    st.subheader("Vitals and Core Metrics")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1.0, 120.0, 30.0, help="Your current age in years.")
        glucose = st.number_input("Glucose (mg/dL)", 50.0, 300.0, 90.0, help="Fasting blood glucose level. Normal range is typically below 100 mg/dL.")
        bmi = st.number_input("BMI (kg/m²)", 10.0, 60.0, 25.0, help="Body Mass Index, calculated from weight and height. Normal is 18.5 - 24.9.")
        chol = st.number_input("Total Cholesterol (mg/dL)", 100.0, 500.0, 200.0, help="Total cholesterol level. Ideal is typically below 200 mg/dL.")
        hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5, help="Average blood sugar level over the past 3 months. Normal is below 5.7%.")

    with col2:
        # Note: Gender input needs to be retrieved first, then mapped to 0/1
        gender_str = st.selectbox("Gender", ["Male", "Female"], help="Biological sex for risk calculation.")
        gender = 0 if gender_str == "Male" else 1

        bp = st.number_input("Blood Pressure (mmHg)", 60.0, 200.0, 120.0, help="A general measure of blood pressure (Systolic is typically used). Normal is < 120.")
        oxy = st.number_input("Oxygen Saturation (%)", 70.0, 100.0, 98.0, help="Percentage of oxygen carried by the blood. Healthy range is 95% to 100%.")
        trig = st.number_input("Triglycerides (mg/dL)", 50.0, 600.0, 150.0, help="Fasting triglycerides level. Ideal is typically below 150 mg/dL.")


    # --- Section 2: Lifestyle & History ---

    st.subheader("Lifestyle and History")
    col3, col4 = st.columns(2)

    with col3:
        smoking_str = st.selectbox("Smoking", ["No", "Yes"], help="Do you currently smoke or have a history of smoking?")
        smoking = 1 if smoking_str == "Yes" else 0

        physical = st.number_input("Physical Activity (Score 0-10)", 0.0, 10.0, 5.0, help="How physically active are you? 0=Sedentary, 10=Highly Active/Daily Exercise.")
        family_str = st.selectbox("Family History of Condition", ["No", "Yes"], help="Do close family members (parents, siblings) have heart disease, diabetes, or cancer?")
        family = 1 if family_str == "Yes" else 0

    with col4:
        alcohol_str = st.selectbox("Alcohol Consumption", ["No", "Yes"], help="Do you consume alcohol regularly?")
        alcohol = 1 if alcohol_str == "Yes" else 0

        diet = st.number_input("Diet Score (0-10)", 0.0, 10.0, 5.0, help="Quality of your diet. 0=Very Poor/Processed, 10=Very Healthy/Balanced.")
        stress = st.number_input("Stress Level (0-10)", 0.0, 10.0, 5.0, help="Perceived average stress level. 0=Relaxed, 10=Extremely Stressed.")
        sleep = st.number_input("Sleep Hours (h)", 0.0, 15.0, 7.0, help="Average hours of sleep per night. Recommended range is 7-9 hours.")

    st.markdown("---")
    submit = st.form_submit_button("✅ Predict")


if submit:
    # Gather all inputs into a single numpy array
    input_vector = [
        age, gender, glucose, bp, bmi, oxy, chol, trig,
        hba1c, smoking, alcohol, physical, diet, family,
        stress, sleep
    ]
    st.session_state["input_data"] = np.array([input_vector])

    # Switch to the result page
    st.switch_page("pages/2_Result.py")
# import streamlit as st
# from bg import apply_bg
# import numpy as np
#
# # Apply custom CSS to make input fields white and the button transparent/themed
# st.markdown("""
# <style>
# /* Targets the input area within all st.number_input widgets and sets it to WHITE */
# div[data-testid="stNumberInput"] input {
#     background-color: #FFFFFF !important;
#     color: #333333; /* Ensure text color is dark on white background */
# }
# /* Targets the wrapper around st.number_input to ensure the entire input box is white */
# div[data-testid="stNumberInput"] > div:first-child {
#     background-color: #FFFFFF !important;
# }
#
# /* Targets the box around st.selectbox and sets it to WHITE */
# div[data-testid="stSelectbox"] > div:first-child {
#     background-color: #FFFFFF !important;
# }
# /* Targets the input display within st.selectbox for consistency */
# div[data-testid="stSelectbox"] input {
#     background-color: #FFFFFF !important;
#     color: #333333;
# }
#
#
# /* Make the entire form container transparent (if it was adding a gray background) */
# div[data-testid="stForm"] {
#     background-color: transparent !important;
#     border: none !important;
#     padding: 0;
# }
#
# /* --- Styling for the Predict Button (Kept transparent) --- */
# div[data-testid="stFormSubmitButton"] button {
#     /* Use !important to override Streamlit's default background and box-shadow */
#     background-color: transparent !important;
#     box-shadow: none !important; /* Remove any default button shadows/gradients */
#
#     color: #4CAF50 !important; /* Text color green */
#     border: 2px solid #4CAF50 !important; /* Green border */
#     font-weight: bold;
#     border-radius: 8px; /* Rounded corners */
#     transition: all 0.2s; /* Smooth transition for hover effects */
# }
# div[data-testid="stFormSubmitButton"] button:hover {
#     background-color: rgba(76, 175, 80, 0.1) !important; /* Light green tint on hover */
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important; /* Subtle shadow on hover */
#     transform: translateY(-1px); /* Slight lift effect */
# }
# </style>
# """, unsafe_allow_html=True)
#
# # Apply background styling (ensure this is called after the CSS or it might overwrite styles)
# apply_bg()
#
# st.title("Patient Input")
#
# with st.form("input_form"):
#     # --- Section 1: Vitals & Core Metrics (2 columns per row) ---
#
#     st.subheader("Vitals and Core Metrics")
#     col1, col2 = st.columns(2)
#
#     with col1:
#         age = st.number_input("Age", 1.0, 120.0, 30.0, help="Your current age in years.")
#         glucose = st.number_input("Glucose (mg/dL)", 50.0, 300.0, 90.0,
#                                   help="Fasting blood glucose level. Normal range is typically below 100 mg/dL.")
#         bmi = st.number_input("BMI (kg/m²)", 10.0, 60.0, 25.0,
#                               help="Body Mass Index, calculated from weight and height. Normal is 18.5 - 24.9.")
#         chol = st.number_input("Total Cholesterol (mg/dL)", 100.0, 500.0, 200.0,
#                                help="Total cholesterol level. Ideal is typically below 200 mg/dL.")
#         hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5,
#                                 help="Average blood sugar level over the past 3 months. Normal is below 5.7%.")
#
#     with col2:
#         # Note: Gender input needs to be retrieved first, then mapped to 0/1
#         gender_str = st.selectbox("Gender", ["Male", "Female"], help="Biological sex for risk calculation.")
#         gender = 0 if gender_str == "Male" else 1
#
#         bp = st.number_input("Blood Pressure (mmHg)", 60.0, 200.0, 120.0,
#                              help="A general measure of blood pressure (Systolic is typically used). Normal is < 120.")
#         oxy = st.number_input("Oxygen Saturation (%)", 70.0, 100.0, 98.0,
#                               help="Percentage of oxygen carried by the blood. Healthy range is 95% to 100%.")
#         trig = st.number_input("Triglycerides (mg/dL)", 50.0, 600.0, 150.0,
#                                help="Fasting triglycerides level. Ideal is typically below 150 mg/dL.")
#
#     # --- Section 2: Lifestyle & History ---
#
#     st.subheader("Lifestyle and History")
#     col3, col4 = st.columns(2)
#
#     with col3:
#         smoking_str = st.selectbox("Smoking", ["No", "Yes"],
#                                    help="Do you currently smoke or have a history of smoking?")
#         smoking = 1 if smoking_str == "Yes" else 0
#
#         physical = st.number_input("Physical Activity (Score 0-10)", 0.0, 10.0, 5.0,
#                                    help="How physically active are you? 0=Sedentary, 10=Highly Active/Daily Exercise.")
#         family_str = st.selectbox("Family History of Condition", ["No", "Yes"],
#                                   help="Do close family members (parents, siblings) have heart disease, diabetes, or cancer?")
#         family = 1 if family_str == "Yes" else 0
#
#     with col4:
#         alcohol_str = st.selectbox("Alcohol Consumption", ["No", "Yes"], help="Do you consume alcohol regularly?")
#         alcohol = 1 if alcohol_str == "Yes" else 0
#
#         diet = st.number_input("Diet Score (0-10)", 0.0, 10.0, 5.0,
#                                help="Quality of your diet. 0=Very Poor/Processed, 10=Very Healthy/Balanced.")
#         stress = st.number_input("Stress Level (0-10)", 0.0, 10.0, 5.0,
#                                  help="Perceived average stress level. 0=Relaxed, 10=Extremely Stressed.")
#         sleep = st.number_input("Sleep Hours (h)", 0.0, 15.0, 7.0,
#                                 help="Average hours of sleep per night. Recommended range is 7-9 hours.")
#
#     st.markdown("---")
#     submit = st.form_submit_button("✅ Predict")
#
# if submit:
#     # Gather all inputs into a single numpy array
#     input_vector = [
#         age, gender, glucose, bp, bmi, oxy, chol, trig,
#         hba1c, smoking, alcohol, physical, diet, family,
#         stress, sleep
#     ]
#     st.session_state["input_data"] = np.array([input_vector])
#
#     # Switch to the result page
#     st.switch_page("pages/2_Result.py")

# import streamlit as st
# from bg import apply_bg
# import numpy as np
#
# # Apply custom CSS to force WHITE background on all input fields
# st.markdown("""
# <style>
# /* --- INPUT FIELDS & SELECT BOXES (Force White Background) --- */
#
# /* 1. Target the actual input box area for number/text inputs */
# div[data-baseweb="base-input"] > div {
#     background-color: #FFFFFF !important;
#     border: 1px solid #CCCCCC !important;
#     color: #333333 !important; /* Ensure text is dark */
# }
#
# /* 2. Target the text inside number/text inputs */
# div[data-baseweb="base-input"] input {
#     color: #333333 !important;
#     background-color: #FFFFFF !important;
# }
#
# /* 3. Target the selectbox dropdown area */
# div[data-baseweb="select"] > div:first-child {
#     background-color: #FFFFFF !important;
#     border: 1px solid #CCCCCC !important;
# }
#
# /* 4. Target the selected text inside the selectbox */
# div[data-baseweb="select"] span {
#     color: #333333 !important;
# }
#
# /* 5. Target the whole column/widget container to ensure NO transparent background bleeds through */
# div[data-testid^="stNumberInput"],
# div[data-testid^="stSelectbox"] {
#     /* If you still see transparency, uncomment the line below: */
#     /* background-color: #FFFFFF !important; */
#     border-radius: 8px;
#     padding: 8px 0; /* Adjust padding to look good */
#     margin-bottom: 5px;
# }
#
#
# /* --- TOOLTIP/HELP TEXT FIX (Force White Background, Dark Text) --- */
# /* This targets the Streamlit tooltip popover element and ensures high contrast */
# .st-emotion-cache-1ujn32p {
#     color: #333333 !important; /* Force dark text color */
#     background-color: #FFFFFF !important; /* Force white background */
#     border: 1px solid #CCCCCC !important;
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Optional: Adds a subtle shadow */
# }
#
#
# /* Make the entire form container transparent */
# div[data-testid="stForm"] {
#     background-color: transparent !important;
#     border: none !important;
#     padding: 0;
# }
#
# /* --- Styling for the Predict Button (Kept transparent) --- */
# div[data-testid="stFormSubmitButton"] button {
#     background-color: transparent !important;
#     box-shadow: none !important;
#
#     color: #4CAF50 !important;
#     border: 2px solid #4CAF50 !important;
#     font-weight: bold;
#     border-radius: 8px;
#     transition: all 0.2s;
# }
# div[data-testid="stFormSubmitButton"] button:hover {
#     background-color: rgba(76, 175, 80, 0.1) !important;
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important;
#     transform: translateY(-1px);
# }
# </style>
# """, unsafe_allow_html=True)
#
# # Apply background styling (ensure this is called after the CSS or it might overwrite styles)
# apply_bg()
#
# st.title("Patient Input")
#
# with st.form("input_form"):
#     # --- Section 1: Vitals & Core Metrics (2 columns per row) ---
#
#     st.subheader("Vitals and Core Metrics")
#     col1, col2 = st.columns(2)
#
#     with col1:
#         age = st.number_input("Age", 1.0, 120.0, 30.0, help="Your current age in years.")
#         glucose = st.number_input("Glucose (mg/dL)", 50.0, 300.0, 90.0,
#                                   help="Fasting blood glucose level. Normal range is typically below 100 mg/dL.")
#         bmi = st.number_input("BMI (kg/m²)", 10.0, 60.0, 25.0,
#                               help="Body Mass Index, calculated from weight and height. Normal is 18.5 - 24.9.")
#         chol = st.number_input("Total Cholesterol (mg/dL)", 100.0, 500.0, 200.0,
#                                help="Total cholesterol level. Ideal is typically below 200 mg/dL.")
#         hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5,
#                                 help="Average blood sugar level over the past 3 months. Normal is below 5.7%.")
#
#     with col2:
#         # Note: Gender input needs to be retrieved first, then mapped to 0/1
#         gender_str = st.selectbox("Gender", ["Male", "Female"], help="Biological sex for risk calculation.")
#         gender = 0 if gender_str == "Male" else 1
#
#         bp = st.number_input("Blood Pressure (mmHg)", 60.0, 200.0, 120.0,
#                              help="A general measure of blood pressure (Systolic is typically used). Normal is < 120.")
#         oxy = st.number_input("Oxygen Saturation (%)", 70.0, 100.0, 98.0,
#                               help="Percentage of oxygen carried by the blood. Healthy range is 95% to 100%.")
#         trig = st.number_input("Triglycerides (mg/dL)", 50.0, 600.0, 150.0,
#                                help="Fasting triglycerides level. Ideal is typically below 150 mg/dL.")
#
#     # --- Section 2: Lifestyle & History ---
#
#     st.subheader("Lifestyle and History")
#     col3, col4 = st.columns(2)
#
#     with col3:
#         smoking_str = st.selectbox("Smoking", ["No", "Yes"],
#                                    help="Do you currently smoke or have a history of smoking?")
#         smoking = 1 if smoking_str == "Yes" else 0
#
#         physical = st.number_input("Physical Activity (Score 0-10)", 0.0, 10.0, 5.0,
#                                    help="How physically active are you? 0=Sedentary, 10=Highly Active/Daily Exercise.")
#         family_str = st.selectbox("Family History of Condition", ["No", "Yes"],
#                                   help="Do close family members (parents, siblings) have heart disease, diabetes, or cancer?")
#         family = 1 if family_str == "Yes" else 0
#
#     with col4:
#         alcohol_str = st.selectbox("Alcohol Consumption", ["No", "Yes"], help="Do you consume alcohol regularly?")
#         alcohol = 1 if alcohol_str == "Yes" else 0
#
#         diet = st.number_input("Diet Score (0-10)", 0.0, 10.0, 5.0,
#                                help="Quality of your diet. 0=Very Poor/Processed, 10=Very Healthy/Balanced.")
#         stress = st.number_input("Stress Level (0-10)", 0.0, 10.0, 5.0,
#                                  help="Perceived average stress level. 0=Relaxed, 10=Extremely Stressed.")
#         sleep = st.number_input("Sleep Hours (h)", 0.0, 15.0, 7.0,
#                                 help="Average hours of sleep per night. Recommended range is 7-9 hours.")
#
#     st.markdown("---")
#     submit = st.form_submit_button("✅ Predict")
#
# if submit:
#     # Gather all inputs into a single numpy array
#     input_vector = [
#         age, gender, glucose, bp, bmi, oxy, chol, trig,
#         hba1c, smoking, alcohol, physical, diet, family,
#         stress, sleep
#     ]
#     st.session_state["input_data"] = np.array([input_vector])
#
#     # Switch to the result page
#     st.switch_page("pages/2_Result.py")