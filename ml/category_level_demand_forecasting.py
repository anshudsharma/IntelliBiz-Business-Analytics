from analytics.database import Database
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score




class DemandForecasting:
    """
    Product Demand Forecasting using Random Forest.
    """

    def __init__(self):
        """
        Initialize database service.
        """
        self.db = Database()



    def get_monthly_category_demand(
        self,
        company_id
    ):
        """
        Fetch monthly category demand.
        """

        query = """
        SELECT
            p.category,

            DATE_FORMAT(
                s.sale_date,
                '%Y-%m'
            ) AS month,

            SUM(
                s.quantity
            ) AS total_quantity

        FROM sales s

        JOIN products p
            ON s.product_id =
            p.product_id

        WHERE s.company_id =
            :company_id

        GROUP BY
            p.category,
            month

        ORDER BY
            p.category,
            month;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id":
                    company_id
            }
        )

        return result    



    def prepare_training_data(
        self,
        company_id
    ):
        """
        Prepare category demand data.
        """

        data = (
            self.get_monthly_category_demand(
                company_id
            )
        )

        data["month"] = pd.to_datetime(
            data["month"]
        )

        data["month_number"] = (
            data["month"].dt.year * 12
            +
            data["month"].dt.month
        )

        encoder = LabelEncoder()

        data["category_encoded"] = (
            encoder.fit_transform(
                data["category"]
            )
        )

        return data    




    def train_model(self, company_id):
        """
        Train demand forecasting model.
        """

        data = self.prepare_training_data(company_id)

        X = data[["category_encoded","month_number"]]

        y = data["total_quantity"]

        X_train, X_test, y_train, y_test = (
            train_test_split(X,y,test_size=0.2,random_state=42)
        )

        model = RandomForestRegressor(n_estimators=100,random_state=42)

        model.fit(X_train,y_train)

        predictions = model.predict(X_test)

        accuracy = (r2_score(y_test,predictions) * 100)

        return {"model": model,"accuracy": round(accuracy,2)}
    


    def forecast_demand(self, company_id):
        """
        Generate demand forecasting summary.
        """

        data = self.prepare_training_data(company_id)

        model_info = self.train_model(company_id)

        category_summary = (data.groupby("category")["total_quantity"].sum().sort_values(ascending=False))

        top_category = (category_summary.index[0])

        top_quantity = int(category_summary.iloc[0])

        return {"top_demand_category":top_category,"historical_quantity":top_quantity, "accuracy":model_info["accuracy"]}
    
    