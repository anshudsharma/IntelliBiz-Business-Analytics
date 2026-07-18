import sys
from pathlib import Path
from app.styles import load_css

project_root = Path(__file__).resolve().parents[2]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import streamlit as st

from ml.sales_forecasting import SalesForecasting
from ml.churn_prediction import ChurnPrediction
from ml.category_level_demand_forecasting import DemandForecasting
from ml.customer_segmentation import CustomerSegmentation
import pandas as pd
import plotly.express as px


from app.auth.session import is_logged_in

if not is_logged_in():

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "login.py"
    )

st.set_page_config(
    page_title="Predictive Analytics",
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


st.title("📈 Predictive Analytics")


# role check whether user is superadmin or not
from app.auth.roles import is_super_admin

if is_super_admin():
    company_id = 1
else:
    company_id = st.session_state.company_id

# ==================================================
# SALES FORECASTING
# ==================================================

sales_forecast = SalesForecasting()

forecast = sales_forecast.forecast_next_month(
    company_id
)

st.subheader(
    "📊 Sales Forecast"
)
st.info(
    """
    Prediction Horizon:
    Revenue forecast for the next month based on historical sales trends.
    """
)
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Predicted Revenue",
        f"${forecast['predicted_revenue']:,.2f}"
    )

with col2:
    st.metric(
        "Forecast Accuracy",
        f"{forecast['accuracy']}%"
    )
st.success(
    f"""
    Revenue is forecasted to reach
    ${forecast['predicted_revenue']:,.2f}
    next month.

    Forecast confidence:
    {forecast['accuracy']}%
    """
)

st.divider()

# ==================================================
# CHURN PREDICTION
# ==================================================

churn_model = ChurnPrediction()

churn = churn_model.predict_churn_risk(
    company_id
)

st.subheader(
    "⚠️ Customer Churn Prediction"
)
st.warning(
    f"""
    Model predicts that approximately
    {churn['predicted_churn_rate']}%
    of customers are at risk of churning based on historical purchasing behavior.
    """
)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "High Risk Customers",
        f"{churn['high_risk_customers']:,}"
    )

with col2:
    st.metric(
        "Predicted Churn Rate",
        f"{churn['predicted_churn_rate']}%"
    )

with col3:
    st.metric(
        "Model Accuracy",
        f"{churn['accuracy']}%"
    )
if churn["predicted_churn_rate"] > 50:

    st.error(
        f"""
        🚨 High Churn Alert

        {churn['high_risk_customers']:,}
        customers are predicted to churn.

        Immediate retention actions
        are strongly recommended.
        """
    )

else:

    st.success(
        "Customer retention is healthy."
    )

st.subheader(
    "📊 Confusion Matrix Heatmap"
)

cm = churn["confusion_matrix"]

confusion_df = pd.DataFrame(
    cm,
    index=[
        "Actual No Churn",
        "Actual Churn"
    ],
    columns=[
        "Predicted No Churn",
        "Predicted Churn"
    ]
)

fig = px.imshow(
    confusion_df,
    text_auto=True,
    aspect="auto",
    labels={
        "x": "Predicted",
        "y": "Actual",
        "color": "Customers"
    },
    title="Customer Churn Model Performance"
)

st.plotly_chart(
    fig,
    width="stretch"
)

correct = cm[0][0] + cm[1][1]
incorrect = cm[0][1] + cm[1][0]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "✅ Correct Predictions",
        f"{correct:,}"
    )

with col2:
    st.metric(
        "❌ Incorrect Predictions",
        f"{incorrect:,}"
    )

# st.info(
#     """
#     Top Left = True Negative

#     Top Right = False Positive

#     Bottom Left = False Negative

#     Bottom Right = True Positive
#     """
# )

st.divider()

# ==================================================
# DEMAND FORECAST
# ==================================================

demand_model = DemandForecasting()

demand = demand_model.forecast_demand(
    company_id
)

st.subheader(
    "📦 Demand Forecast"
)
st.info(
    f"""
    Highest expected demand remains in
    {demand['top_demand_category'].replace('_',' ').title()}
    based on historical sales patterns.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Top Demand Category",
        demand["top_demand_category"]
        .replace("_", " ")
        .title()
    )

with col2:
    st.metric(
        "Historical Quantity",
        demand["historical_quantity"]
    )

with col3:
    st.metric(
        "Model Accuracy",
        f"{demand['accuracy']}%"
    )

st.divider()

# ==================================================
# CUSTOMER SEGMENTS
# ==================================================

segment_model = CustomerSegmentation()

segments = segment_model.analyze_clusters(
    company_id
)

st.subheader(
    "👥 Customer Segmentation"
)

st.dataframe(
    segments,
    width="stretch"
)


