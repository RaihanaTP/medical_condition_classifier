import streamlit as st
from bg import apply_bg

apply_bg()

st.markdown(
    "<h1 style='text-align:center; font-size:50px;'> HealthLens</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<div style='text-align:center; font-size:22px;'>
Your intelligent health companion that predicts conditions from your vitals, habits, and lifestyle.<br>
Navigate through the app to explore predictions with ease.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("➡️ Start your prediction journey:")

st.page_link("pages/1_Input.py", label="Proceed to Patient Input", icon="📝")