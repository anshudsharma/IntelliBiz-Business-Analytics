from dotenv import load_dotenv
from google import genai
import os

from analytics.kpi_engine import KPIEngine
from analytics.sales_analysis import SalesAnalysis
from analytics.customer_analysis import CustomerAnalysis
from analytics.product_analysis import ProductAnalysis
from analytics.review_analysis import ReviewAnalysis

from ml.sales_forecasting import SalesForecasting
from ml.customer_segmentation import CustomerSegmentation
from ml.churn_prediction import ChurnPrediction
from ml.category_level_demand_forecasting import DemandForecasting
from sqlalchemy import text



load_dotenv()


class AIAdvisor:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv(
                "GOOGLE_API_KEY"
            )
        )

        self.kpi = KPIEngine()

        self.sales = SalesAnalysis()

        self.customer = CustomerAnalysis()

        self.product = ProductAnalysis()

        self.review = ReviewAnalysis()

        self.sales_forecast = (
            SalesForecasting()
        )

        self.customer_segment = (
            CustomerSegmentation()
        )

        self.churn = (
            ChurnPrediction()
        )

        self.demand = (
            DemandForecasting()
        )




    def collect_business_data(self,company_id):
        revenue = self.kpi.get_total_revenue(company_id)

        profit = self.kpi.get_total_profit(company_id)

        orders = self.kpi.get_total_orders(company_id)

        margin = self.kpi.get_profit_margin(company_id)

        forecast = (self.sales_forecast.forecast_next_month(company_id))

        churn = (self.churn.predict_churn_risk(company_id))

        demand = (self.demand.forecast_demand(company_id))   
        segments = (self.customer_segment.analyze_clusters(company_id))




        return {
            "revenue": float(revenue),
            "profit": float(profit),
            "orders": int(orders),
            "profit_margin": float(margin),

            "sales_forecast": forecast,

            "churn": churn,

            "demand": demand,

            "customer_segments":
                segments.to_dict()
        }
    
    def generate_recommendations(
        self,
        company_id
    ):

        data = self.collect_business_data(
            company_id
        )

        prompt_data = f"""
    Revenue: {data['revenue']}

    Profit: {data['profit']}

    Orders: {data['orders']}

    Profit Margin: {data['profit_margin']}%

    Sales Forecast:
    Predicted Revenue:
    {data['sales_forecast']['predicted_revenue']}

    Forecast Accuracy:
    {data['sales_forecast']['accuracy']}%

    Churn:
    Actual Churn:
    {data['churn']['actual_churn_rate']}%

    Predicted Churn:
    {data['churn']['predicted_churn_rate']}%

    Demand:
    Top Category:
    {data['demand']['top_demand_category']}

    Historical Quantity:
    {data['demand']['historical_quantity']}
    """

        prompt = f"""
    You are an expert Business Intelligence Consultant.

    Analyze the following business data and provide:

    1. Executive Summary
    2. Key Risks
    3. Growth Opportunities
    4. Strategic Recommendations
    5. Priority Actions for the next 30 days

    Business Data:

    {prompt_data}
    """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        report = response.text

        self.save_report(
            company_id,
            report
        )

        return report
    




    def save_report(
        self,
        company_id,
        report
    ):
        """
        Save AI-generated report to database.
        """

        query = text("""
        INSERT INTO generated_reports
        (
            company_id,
            report_type,
            report_content
        )
        VALUES
        (
            :company_id,
            :report_type,
            :report_content
        )
        """)

        with self.kpi.db.engine.begin() as connection:

            connection.execute(
                query,
                {
                    "company_id": company_id,
                    "report_type": "AI Advisor",
                    "report_content": report
                }
            )

        print(
            "AI report saved successfully."
        )