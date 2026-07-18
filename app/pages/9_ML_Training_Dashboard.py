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

st.title("⚙️ ML Training Dashboard")

st.info(
    """
    Monitor machine learning
    training performance,
    model health and
    retraining activity.

    ⚠ Live training execution
    is currently under development.
    """
)


