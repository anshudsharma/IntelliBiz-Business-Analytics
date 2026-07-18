import sys
from pathlib import Path
from app.styles import load_css

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

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
    page_title="KPI Dashboard",
    page_icon="📈",
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


st.title("📈 KPI Dashboard")


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
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Revenue",
        f"${revenue:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${profit:,.2f}"
    )

with col3:
    st.metric(
        "Total Orders",
        f"{orders:,}"
    )

with col4:
    st.metric(
        "Profit Margin",
        f"{margin:.2f}%"
    )


st.markdown("---")

monthly_revenue = kpi.get_monthly_revenue(
    company_id
)
# Remove incomplete last month
monthly_revenue = monthly_revenue.iloc[:-1]

st.subheader(
    "📈 Monthly Revenue Trend"
)

st.line_chart(
    monthly_revenue.set_index("month")[
        "total_revenue"
    ]
)


monthly_profit = (
    kpi.get_monthly_profit(
        company_id
    )
)

# Remove incomplete last month
monthly_profit = monthly_profit.iloc[:-1]

st.subheader(
    "💰 Monthly Profit Trend"
)

st.line_chart(
    monthly_profit.set_index(
        "month"
    )[
        "total_profit"
    ]
)