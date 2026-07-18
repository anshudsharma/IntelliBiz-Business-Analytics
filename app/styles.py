import streamlit as st

def load_css():

    st.markdown("""
    <style>

    div[data-testid="stMetric"] {
        background-color: #111827;
        border: 1px solid #374151;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.25);
    }

    div[data-testid="stMetric"]:hover {
        border: 1px solid #60A5FA;
    }

    </style>
    """,
    unsafe_allow_html=True)