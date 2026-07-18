from analytics.database import Database

import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,confusion_matrix)


class ChurnPrediction:
    """
    Customer Churn Prediction for IntelliBiz.
    """

    def __init__(self):
        """
        Initialize database service.
        """
        self.db = Database()

    def get_customer_data(self, company_id):
        """
        Fetch customer data for churn analysis.
        """

        query = """
        SELECT
            customer_id,

            COUNT(
                DISTINCT order_id
            ) AS total_orders,

            ROUND(
                SUM(revenue),
                2
            ) AS total_revenue,

            ROUND(
                AVG(revenue),
                2
            ) AS average_order_value,

            MAX(sale_date)
                AS last_purchase_date

        FROM sales

        WHERE company_id = :company_id

        GROUP BY customer_id;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id
            }
        )

        return result

    def prepare_churn_data(self, company_id):
        """
        Prepare churn dataset using recency.
        """

        data = self.get_customer_data(
            company_id
        )

        data["last_purchase_date"] = pd.to_datetime(
            data["last_purchase_date"]
        )

        latest_date = data[
            "last_purchase_date"
        ].max()

        data["days_since_last_purchase"] = (
            latest_date
            - data["last_purchase_date"]
        ).dt.days

        data["churn"] = (
            data["days_since_last_purchase"] > 180
        ).astype(int)

        return data

    def train_model(self, company_id):
        """
        Train churn prediction model.
        """

        data = self.prepare_churn_data(
            company_id
        )

        X = data[
            [
                "total_orders",
                "total_revenue",
                "average_order_value"
            ]
        ]

        y = data["churn"]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        accuracy = (
            accuracy_score(
                y_test,
                predictions
            ) * 100
        )
        cm = confusion_matrix(
            y_test,
            predictions
        )
        

        return {"model": model,"accuracy": round(accuracy,2),"confusion_matrix":cm.tolist()}
    

    def predict_churn_risk(self, company_id):
        """
        Predict customers likely to churn.
        """

        data = self.prepare_churn_data(
            company_id
        )

        model_info = self.train_model(
            company_id
        )

        model = model_info["model"]

        X = data[
            [
                "total_orders",
                "total_revenue",
                "average_order_value"
            ]
        ]

        predictions = model.predict(X)

        data["predicted_churn"] = predictions

        high_risk_customers = (
            data["predicted_churn"] == 1
        ).sum()

        total_customers = len(data)

        churn_rate = round(
            (
                high_risk_customers
                / total_customers
            ) * 100,
            2
        )

        actual_churn_rate = round((data["churn"].sum()/ len(data)) * 100,2)

        return {
            "high_risk_customers":
                int(high_risk_customers),

            "total_customers":
                int(total_customers),

            "actual_churn_rate":
                float(actual_churn_rate),

            "predicted_churn_rate":
                float(churn_rate),

            "accuracy":
                float(model_info["accuracy"]),

            "confusion_matrix":
                model_info["confusion_matrix"]
        }
    