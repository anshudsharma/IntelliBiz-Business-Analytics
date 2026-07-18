import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))


import streamlit as st
from datetime import datetime

from app.styles import load_css

from analytics.kpi_engine import KPIEngine

from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )




st.set_page_config(
    page_title="IntelliBiz",
    page_icon="📊",
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

st.image(
    "assets/banner.png",
    use_container_width=True
)
st.caption(
    f"Last Updated: {datetime.now().strftime('%d %b %Y %H:%M')}"
)
# ==========================================
# DATA
# ==========================================


# role check whether user is superadmin or not
from app.auth.roles import is_super_admin

if is_super_admin():
    company_id = 1
else:
    company_id = st.session_state.company_id


kpi = KPIEngine()

revenue = kpi.get_total_revenue(
    company_id
)

profit = kpi.get_total_profit(
    company_id
)

orders = kpi.get_total_orders(
    company_id
)

margin = kpi.get_profit_margin(
    company_id
)

# ==========================================
# HEADER
# ==========================================


st.divider()

# ==========================================
# EXECUTIVE KPI OVERVIEW
# ==========================================

st.markdown(
    "### 📈 Executive Overview"
)

col1, col2, col3, col4 = st.columns(4)

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
        "Profit Margin",
        f"{margin:.2f}%"
    )

st.divider()

st.markdown(
    "### 🚀 Platform Capabilities"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Analytics Modules",
        "4"
    )

with col2:
    st.metric(
        "ML Models",
        "4"
    )

with col3:
    st.metric(
        "AI Engine",
        "Gemini"
    )

with col4:
    st.metric(
        "Architecture",
        "Multi-Tenant Ready"
    )

# ==========================================
# QUICK ACCESS
# ==========================================

st.divider()
st.markdown(
    "## ⚡ Platform Modules"
)

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.page_link(
            "pages/1_KPI_Dashboard.py",
            label="📊 KPI Dashboard"
        )

        st.caption(
            "Track Revenue, Profit, Orders and KPIs."
        )
        st.write("")
    with st.container(border=True):

        st.page_link(
            "pages/2_Sales_Analytics.py",
            label="💰 Sales Analytics"
        )

        st.caption(
            "Analyze sales trends and product performance."
        )
with col2:

    with st.container(border=True):

        st.page_link(
            "pages/3_Customer_Analytics.py",
            label="👥 Customer Analytics"
        )

        st.caption(
            "Customer behavior and segmentation insights."
        )
        st.write("")
    with st.container(border=True):

        st.page_link(
            "pages/6_Predictive_Analytics.py",
            label="📈 Predictive Analytics"
        )

        st.caption(
            "Forecast revenue, demand and churn."
        )

with col3:

    with st.container(border=True):

        st.page_link(
            "pages/4_AI_Advisor.py",
            label="🤖 AI Advisor"
        )

        st.caption(
            "AI-powered business recommendations."
        )
        st.write("")
    with st.container(border=True):

        st.page_link(
            "pages/5_Generated_Reports.py",
            label="📄 Generated Reports"
        )

        st.caption(
            "View previously generated AI reports."
        )


# ==========================================
# ABOUT
# ==========================================

st.divider()

st.markdown(
    "### 🤖 About IntelliBiz"
)

st.info(
    """
    IntelliBiz combines Business Intelligence,
    Machine Learning and Generative AI to help
    organizations analyze performance,
    forecast trends, predict customer behavior,
    and generate strategic recommendations.
    """
)
