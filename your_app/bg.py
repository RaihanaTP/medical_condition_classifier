# import streamlit as st
# import base64
# import os
#
# st.set_page_config(layout="wide")
#
# def apply_bg(image_file="ml1_img.png"):
#     if os.path.exists(image_file):
#         with open(image_file, "rb") as f:
#             encoded = base64.b64encode(f.read()).decode()
#         st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background: url("data:image/jpeg;base64,{encoded}");
#                 background-size: cover;
#                 background-position: center;
#                 background-attachment: fixed;
#                 color: black !important;
#             }}
#             h1, h2, h3, p, label {{
#                 color: black !important;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
import streamlit as st
import base64
import os

st.set_page_config(layout="wide")


# Set the correct image file name to ml1_img.png based on the folder structure
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
                background: url("data:image/png;base64,{encoded}"); /* Using image/png */
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            /* --- TEXT & LABELS (BLACK) --- */
            h1, h2, h3, p, label, .stMarkdown, a, .css-1d391kg div, .css-1d391kg span, .css-1d391kg a, .streamlit-p {{
                color: black !important;
            }}

            /* Remove default main container background to ensure transparency */
            .main > div,
            section[data-testid="stSidebar"] > div,
            div[data-testid="stForm"] > div
            {{
                background-color: transparent !important;
            }}

            /* --- INPUT WIDGET CONTAINERS (Light Transparent Overlay) --- */
            .stTextInput, .stNumberInput, .stSelectbox {{
                background-color: rgba(255, 255, 255, 0.2) !important; /* Very light transparent white container */
                border-radius: 0.5rem;
                padding: 0.5rem;
            }}

            /* --- ACTUAL INPUT FIELDS (Dark Transparent Gray) --- */
            /* This selector now covers number_input (base-input), selectbox, and textinput */
            div[data-baseweb="input"] > div,
            div[data-baseweb="select"] > div,
            div[data-baseweb="base-input"] > div
            {{
                background-color: rgba(0, 0, 0, 0.5) !important; /* Darker transparent gray for the actual input area */
                color: white !important; /* Text inside the input field should be white */
                border: 1px solid rgba(255, 255, 255, 0.3); /* Subtle white border */
                border-radius: 0.4rem;
            }}

            /* Text inside the input fields (user input/selected value) */
            div[data-baseweb="input"] input,
            div[data-baseweb="select"] span {{
                color: white !important;
            }}

            /* --- BUTTONS (Dark Transparent Gray) --- */
            .stButton>button,
            .stPageLink > a,
            div[data-testid="stForm"] .stButton>button /* Target buttons inside forms */
            {{
                background-color: rgba(0, 0, 0, 0.5) !important; /* Dark transparent gray button */
                color: white !important; /* Button text is white for contrast */
                font-weight: bold;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 0.5rem;
                padding: 0.75rem 1.5rem;
            }}

            /* Hover effect for buttons */
            .stButton>button:hover, .stPageLink > a:hover {{
                background-color: rgba(0, 0, 0, 0.7) !important;
            }}

            </style>
            """,
            unsafe_allow_html=True
        )