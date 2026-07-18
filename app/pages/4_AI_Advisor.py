# This page will:

# Collect Analytics Data
# Collect ML Predictions
# Send to Gemini
# Display Business Recommendations

import sys
from pathlib import Path
from app.styles import load_css
from analytics.kpi_engine import KPIEngine


project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from ai.advisory import AIAdvisor

from app.auth.session import is_logged_in


if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )


st.set_page_config(
    page_title="AI Advisor",
    page_icon="🤖",
    layout="wide"
)
load_css()


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


# ==========================
# USER INFO
# ==========================

st.sidebar.markdown("---")

st.sidebar.write(
    f"👤 {st.session_state.full_name}"
)

st.sidebar.caption(
    st.session_state.role
)

# ==========================
# LOGOUT
# ==========================

if st.sidebar.button(
    "🚪 Logout"
):

    st.session_state.clear()

    st.switch_page(
        "login.py"
    )

#Protect AI Advisor
from app.auth.roles import (is_super_admin,is_company_admin)
if not (
    is_super_admin()
    or
    is_company_admin()
):

    st.error(
        "Access Denied."
    )

    st.stop()



st.title("🤖 AI Business Advisor")

st.info(
    """
    Generate AI-powered business insights,
    recommendations and strategic actions
    based on analytics and machine learning.
    """
)

st.subheader(
    "📈 Business Snapshot"
)

col1, col2, col3, col4 = st.columns(4)

st.divider()


# role check whether user is superadmin or not
from app.auth.roles import is_super_admin

if is_super_admin():
    company_id = 1
else:
    company_id = st.session_state.company_id

kpi = KPIEngine()

revenue = kpi.get_total_revenue(company_id)
profit = kpi.get_total_profit(company_id)
orders = kpi.get_total_orders(company_id)
margin = kpi.get_profit_margin(company_id)

with col1:
    st.metric(
        "Revenue",
        f"${revenue:,.0f}"
    )

with col2:
    st.metric(
        "Profit",
        f"${profit:,.0f}"
    )

with col3:
    st.metric(
        "Orders",
        f"{orders:,}"
    )

with col4:
    st.metric(
        "Margin",
        f"{margin:.2f}%"
    )


advisor = AIAdvisor()

if st.button(
    "Generate Business Report"
):

    with st.spinner(
        "Analyzing business data..."
    ):

        report = (
            advisor.generate_recommendations(
                company_id
            )
        )

    st.success(
        "Analysis Complete!"
    )

    st.write(report)