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
    page_title="Data Upload Portal",
    page_icon="📁",
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

    st.error(
        "Access Denied."
    )

    st.stop()


st.title("📁 Business Data Upload Portal")

st.info(
    """
    Upload company datasets to power
    analytics, machine learning forecasts,
    and AI-generated business recommendations.

    ! Upload processing is currently
    under development.
    """
)



st.subheader(
    "📤 Upload Company Data"
)

sales_file = st.file_uploader(
    "Upload Sales Dataset",
    type=["csv"]
)

customers_file = st.file_uploader(
    "Upload Customers Dataset",
    type=["csv"]
)

products_file = st.file_uploader(
    "Upload Products Dataset",
    type=["csv"]
)

reviews_file = st.file_uploader(
    "Upload Reviews Dataset",
    type=["csv"]
)




st.divider()

st.subheader(
    "📋 Required Dataset Structure"
)

st.dataframe(
    {
        "Dataset": [
            "Sales",
            "Customers",
            "Products",
            "Reviews"
        ],
        "Required": [
            "order_id, customer_id, product_id, revenue",
            "customer_id, city, state",
            "product_id, category",
            "review_id, rating"
        ]
    },
    width="stretch"
)



if st.button(
    "🚀 Upload Data",
    use_container_width=True
):

    st.warning(
        """
        Upload processing module
        is currently under development.

        Coming Soon:
        • Automatic validation
        • ETL processing
        • Data quality checks
        • Instant dashboard updates
        """
    )



st.divider()

st.subheader(
    "🛣 Future Enhancements"
)

st.success(
    """
    Planned Features:

    ✅ CSV Validation

    ✅ Automated ETL Pipeline

    ✅ Data Quality Scoring

    ✅ Real-Time Dashboard Refresh

    ✅ Multi-Tenant Upload Support

    ✅ AI-Powered Data Cleaning
    """
)