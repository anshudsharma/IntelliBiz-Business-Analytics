import sys
from pathlib import Path
from app.styles import load_css


project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from analytics.customer_analysis import CustomerAnalysis

from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="👥",
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


st.title("👥 Customer Analytics")

customer = CustomerAnalysis()


# role check whether user is superadmin or not
from app.auth.roles import is_super_admin

if is_super_admin():
    company_id = 1
else:
    company_id = st.session_state.company_id

total_customers = (customer.get_total_customers(company_id))

repeat_rate = (customer.get_repeat_customer_rate(company_id))

clv = (customer.get_customer_lifetime_value(company_id))

frequency = (customer.get_customer_purchase_frequency(company_id))

regions = (customer.get_customer_regions(company_id))

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        f"{int(total_customers.iloc[0]['total_customers']):,}"
    )

with col2:
    st.metric(
        "Repeat Rate",
        f"{repeat_rate.iloc[0]['repeat_customer_rate']}%"
    )

with col3:
    st.metric(
        "Customer LTV",
        f"${clv.iloc[0]['customer_lifetime_value']}"
    )

with col4:
    st.metric(
        "Purchase Frequency",
        f"{frequency.iloc[0]['purchase_frequency']}"
    )

st.divider()

st.subheader(
    "🌎 Customer Distribution by City"
)

st.bar_chart(
    regions.set_index("city")[
        "total_customers"
    ]
)

st.subheader(
    "📋 Top Customer Regions"
)

st.dataframe(
    regions,
    width="stretch"
)