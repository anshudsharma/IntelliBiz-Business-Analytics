from analytics.database import Database
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sqlalchemy import text
import pandas as pd



class SalesForecasting:
    """
    Sales Forecasting Model for IntelliBiz.
    """

    def __init__(self):
        self.db = Database()

    def get_monthly_revenue(self, company_id):
        """
        Fetch monthly revenue trend.
        """

        query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            ROUND(SUM(revenue), 2) AS revenue
        FROM sales
        WHERE company_id = :company_id
        GROUP BY month
        ORDER BY month;
        """

        return self.db.execute_query(
            query,
            {"company_id": company_id}
        )




    def prepare_training_data(self, company_id):
        """
        Prepare monthly revenue data.
        """

        data = self.get_monthly_revenue(
            company_id
        )

        # Remove partial months
        data = data.iloc[1:-1].copy()

        # Remove extremely small revenue months
        data = data[
            data["revenue"] > 1000
        ].copy()

        data.reset_index(
            drop=True,
            inplace=True
        )

        data["month_number"] = range(
            1,
            len(data) + 1
        )

        return data
    


    def train_model(self, company_id):
        """
        Train sales forecasting model.
        """

        data = self.prepare_training_data(
            company_id
        )

        X = data[["month_number"]]

        y = data["revenue"]

        model = LinearRegression()

        model.fit(X, y)

        predictions = model.predict(X)

        accuracy = (
            r2_score(
                y,
                predictions
            ) * 100
        )

        return {
            "model": model,
            "accuracy": round(
                accuracy,
                2
            )
        }
    




    def forecast_next_month(self, company_id):
        """
        Predict next month's revenue.
        """

        trained_model = self.train_model(
            company_id
        )

        model = trained_model["model"]

        data = self.prepare_training_data(
            company_id
        )

        next_month = len(data) + 1

        prediction = model.predict(
            pd.DataFrame(
                {
                    "month_number": [next_month]
                }
            )
        )[0]

        return {
            "predicted_revenue": round(
                float(prediction),
                2
            ),
            "accuracy": trained_model[
                "accuracy"
            ]
        }

    def save_prediction(self, company_id):
        """
        Save forecast result into ml_predictions table.
        """

        forecast = self.forecast_next_month(
            company_id
        )

        query = text("""
        INSERT INTO ml_predictions
        (
            company_id,
            model_name,
            prediction_result,
            accuracy
        )
        VALUES
        (
            :company_id,
            :model_name,
            :prediction_result,
            :accuracy
        )
        """)

        with self.db.engine.begin() as connection:

            connection.execute(
                query,
                {
                    "company_id": company_id,
                    "model_name":
                        "sales_forecasting",

                    "prediction_result":
                        str(
                            forecast[
                                "predicted_revenue"
                            ]
                        ),

                    "accuracy":
                        forecast[
                            "accuracy"
                        ]
                }
            )

        return forecast