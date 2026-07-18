import sys
from pathlib import Path
from app.styles import load_css

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )

st.set_page_config(
    page_title="Model Manager",
    page_icon="🧠",
    layout="wide"
)

load_css()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "assets/logo.png",
    width=100
)

st.sidebar.markdown("---")

st.sidebar.success(
    "IntelliBiz v1.0"
)

st.sidebar.caption(
    "AI + BI + ML Platform"
)

st.sidebar.markdown("---")

st.sidebar.write(
    f"👤 {st.session_state.full_name}"
)

st.sidebar.caption(
    st.session_state.role
)

if st.sidebar.button(
    "🚪 Logout"
):
    st.session_state.clear()
    st.switch_page("login.py")

from app.auth.roles import (
    is_super_admin,
    is_company_admin
)

if not (
    is_super_admin()
    or
    is_company_admin()
):

    st.error("Access Denied.")
    st.stop()

# ==========================================
# PAGE HEADER
# ==========================================

st.title("🧠 Model Manager")

st.info(
    """
    Manage Machine Learning models,
    monitor performance and prepare
    models for retraining.

    ⚠ Advanced model retraining is
    currently under development.
    """
)

# ==========================================
# MODEL OVERVIEW
# ==========================================

st.subheader(
    "📊 Active Models"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Models",
        "4"
    )

with col2:
    st.metric(
        "Status",
        "Active"
    )

with col3:
    st.metric(
        "Environment",
        "Production"
    )

with col4:
    st.metric(
        "Version",
        "v1.0"
    )

st.divider()

# ==========================================
# SALES FORECASTING
# ==========================================

with st.container(border=True):

    st.subheader(
        "📈 Sales Forecasting"
    )

    st.write(
        "Predict future revenue using historical sales trends."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Accuracy",
            "83%"
        )

    with col2:
        st.metric(
            "Status",
            "Active"
        )

    if st.button(
        "Retrain Sales Forecasting"
    ):
        st.info(
            "Retraining module under development."
        )

# ==========================================
# CHURN PREDICTION
# ==========================================

with st.container(border=True):

    st.subheader(
        "⚠️ Churn Prediction"
    )

    st.write(
        "Predict customers likely to stop purchasing."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Accuracy",
            "91%"
        )

    with col2:
        st.metric(
            "Status",
            "Active"
        )

    if st.button(
        "Retrain Churn Model"
    ):
        st.info(
            "Retraining module under development."
        )

# ==========================================
# CUSTOMER SEGMENTATION
# ==========================================

with st.container(border=True):

    st.subheader(
        "👥 Customer Segmentation"
    )

    st.write(
        "Cluster customers into behavioral groups."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Clusters",
            "3"
        )

    with col2:
        st.metric(
            "Status",
            "Active"
        )

    if st.button(
        "Retrain Segmentation Model"
    ):
        st.info(
            "Retraining module under development."
        )

# ==========================================
# DEMAND FORECASTING
# ==========================================

with st.container(border=True):

    st.subheader(
        "📦 Demand Forecasting"
    )

    st.write(
        "Forecast product category demand."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Accuracy",
            "88%"
        )

    with col2:
        st.metric(
            "Status",
            "Active"
        )

    if st.button(
        "Retrain Demand Model"
    ):
        st.info(
            "Retraining module under development."
        )

# ==========================================
# ROADMAP
# ==========================================

st.divider()


