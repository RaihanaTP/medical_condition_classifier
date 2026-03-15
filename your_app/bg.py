import streamlit as st
import base64
import os

st.set_page_config(layout="wide")


def apply_bg(image_file="ml1_img.png"):
    if os.path.exists(image_file):
        try:
            with open(image_file, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
        except Exception as e:
            st.error(f"Error reading background image: {e}")
            return

        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            h1, h2, h3, p, label, .stMarkdown, a, .css-1d391kg div, .css-1d391kg span, .css-1d391kg a, .streamlit-p {{
                color: black !important;
            }}

            .main > div,
            section[data-testid="stSidebar"] > div,
            div[data-testid="stForm"] > div
            {{
                background-color: transparent !important;
            }}

            .stTextInput, .stNumberInput, .stSelectbox {{
                background-color: rgba(255, 255, 255, 0.2) !important;
                border-radius: 0.5rem;
                padding: 0.5rem;
            }}

            div[data-baseweb="input"] > div,
            div[data-baseweb="select"] > div,
            div[data-baseweb="base-input"] > div
            {{
                background-color: rgba(0, 0, 0, 0.5) !important;
                color: white !important;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 0.4rem;
            }}

            div[data-baseweb="input"] input,
            div[data-baseweb="select"] span {{
                color: white !important;
            }}

            .stButton>button,
            .stPageLink > a,
            div[data-testid="stForm"] .stButton>button
            {{
                background-color: rgba(0, 0, 0, 0.5) !important;
                color: white !important;
                font-weight: bold;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 0.5rem;
                padding: 0.75rem 1.5rem;
            }}

            .stButton>button:hover, .stPageLink > a:hover {{
                background-color: rgba(0, 0, 0, 0.7) !important;
            }}

            </style>
            """,
            unsafe_allow_html=True
        )