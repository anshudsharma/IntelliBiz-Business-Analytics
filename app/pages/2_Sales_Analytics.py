import sys
from pathlib import Path
from app.styles import load_css
project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from analytics.sales_analysis import SalesAnalysis

from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )

st.set_page_config(
    page_title="Sales Analytics",
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


st.title("📊 Sales Analytics")


# role check whether user is superadmin or not
from app.auth.roles import is_super_admin

if is_super_admin():
    company_id = 1
else:
    company_id = st.session_state.company_id

sales = SalesAnalysis()

top_selling = sales.get_top_selling_products(
    company_id
)

top_revenue = sales.get_top_revenue_products(
    company_id
)

top_profit = sales.get_most_profitable_products(
    company_id
)

sales_category = sales.get_sales_by_category(
    company_id
).head(15)

sales_region = sales.get_sales_by_region(
    company_id
).head(10)

st.subheader(
    "🏆 Top Selling Products"
)

st.dataframe(
    top_selling,
    use_container_width=True
)

st.subheader(
    "💰 Top Revenue Products"
)

st.dataframe(
    top_revenue,
    use_container_width=True
)

st.subheader(
    "📈 Most Profitable Products"
)

st.dataframe(
    top_profit,
    use_container_width=True
)



st.subheader(
    "📦 Revenue by Category"
)

st.bar_chart(
    sales_category
    .set_index("category")
    ["total_revenue"]
)
st.subheader(
    "💰 Profit by Category"
)

st.bar_chart(
    sales_category
    .set_index("category")
    ["total_profit"]
)


st.subheader(
    "🌎 Top Revenue Regions"
)

st.bar_chart(
    sales_region
    .set_index("city")
    ["total_revenue"]
)


st.subheader(
    "📋 Category Performance"
)

st.dataframe(
    sales_category,
    width="stretch"
)