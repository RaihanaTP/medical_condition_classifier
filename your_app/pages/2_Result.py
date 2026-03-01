
import streamlit as st
import numpy as np
import pickle
from bg import apply_bg

apply_bg()

st.title("🩺 Prediction Result")

# Check if input data exists
if "input_data" not in st.session_state:
    st.error("No input data found. Please go to the Input page.")
    st.page_link("Input.py", label="Go to Input Page", icon="🔙")
    st.stop()

# Load model + scaler
model = pickle.load(open("modelXGB1.sav", "rb"))
scaler = pickle.load(open("scaler1.sav", "rb"))

label_map = {
    0: "Arthritis", 1: "Asthma", 2: "Cancer",
    3: "Diabetes", 4: "Healthy", 5: "Hypertension", 6: "Obesity"
}

input_data = st.session_state["input_data"]
scaled = scaler.transform(input_data)

pred = model.predict(scaled)[0]
prob = model.predict_proba(scaled)[0]

condition = label_map[int(pred)]
confidence = np.max(prob) * 100

st.subheader(f"✅ Predicted Condition: **{condition}**")
st.write(f"Confidence: **{confidence:.2f}%**")

st.write("### Probability Breakdown:")
for c, p in zip(label_map.values(), prob):
    st.write(f"- {c}: **{p*100:.2f}%**")
