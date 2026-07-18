from analytics.database import Database
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class CustomerSegmentation:
    """
    Customer Segmentation using K-Means Clustering.
    """

    def __init__(self):
        self.db = Database()

    def get_customer_data(self, company_id):
        """
        Fetch customer metrics for clustering.
        """

        query = """
        SELECT
            customer_id,
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(SUM(revenue), 2) AS total_revenue,
            ROUND(AVG(revenue), 2) AS average_order_value
        FROM sales
        WHERE company_id = :company_id
        GROUP BY customer_id
        """

        return self.db.execute_query(
            query,
            {"company_id": company_id}
        )
    


    def segment_customers(self, company_id):
        """
        Segment customers using K-Means clustering.
        """

        data = self.get_customer_data(
            company_id
        )

        features = data[
            [
                "total_orders",
                "total_revenue",
                "average_order_value"
            ]
        ]

        scaler = StandardScaler()

        scaled_features = scaler.fit_transform(
            features
        )

        kmeans = KMeans(
            n_clusters=3,
            random_state=42,
            n_init=10
        )

        data["cluster"] = kmeans.fit_predict(
            scaled_features
        )

        return data
    

    def analyze_clusters(self, company_id):
        """
        Analyze customer clusters.
        """

        data = self.segment_customers(
            company_id
        )

        cluster_summary = (
            data.groupby("cluster")
            [
                [
                    "total_revenue",
                    "average_order_value"
                ]
            ]
            .mean()
            .round(2)
        )

        customer_counts = (
            data.groupby("cluster")
            .size()
        )

        cluster_summary["customer_count"] = (
            customer_counts
        )

        # Determine cluster quality based on spending

        sorted_clusters = (
            cluster_summary["average_order_value"]
            .sort_values()
            .index
            .tolist()
        )

        segment_mapping = {
            sorted_clusters[0]: "At-Risk Customers",
            sorted_clusters[1]: "Regular Customers",
            sorted_clusters[2]: "VIP Customers"
        }

        cluster_summary.index = (
            cluster_summary.index.map(
                segment_mapping
            )
        )
        cluster_summary = (
            cluster_summary[
                [
                    "customer_count",
                    "total_revenue",
                    "average_order_value"
                ]
            ]
        )
        return cluster_summary
