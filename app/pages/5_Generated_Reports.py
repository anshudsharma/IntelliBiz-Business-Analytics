import sys
from pathlib import Path
from app.styles import load_css
project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st
from analytics.database import Database

from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )


st.set_page_config(
    page_title="Generated Reports",
    page_icon="📄",
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

#Protect Generated Reports
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



st.title("📄 Generated Reports")

db = Database()

reports = db.execute_query("""
SELECT
    report_id,
    report_type,
    generated_at,
    report_content
FROM generated_reports
ORDER BY report_id DESC
""")

if reports.empty:
    st.warning("No reports found.")
    st.stop()
else:

    reports["label"] = (
        "Report #"
        + reports["report_id"].astype(str)
        + " | "
        + reports["generated_at"].astype(str)
    )

    selected_label = st.selectbox(
        "Select Report",
        reports["label"]
    )

    report = reports[
        reports["label"] == selected_label
    ].iloc[0]

st.subheader(
    "📋 Report Details"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Report ID",
        report["report_id"]
    )

with col2:
    st.metric(
        "Type",
        report["report_type"]
    )

with col3:
    st.metric(
        "Generated",
        str(report["generated_at"])[:10]
    )

st.divider()

st.subheader(
    "🤖 AI Report Viewer"
)

st.markdown(
    report["report_content"]
)

st.download_button(
    label="⬇ Download Report",
    data=report["report_content"],
    file_name=f"report_{report['report_id']}.txt",
    mime="text/plain"
)
