from analytics.database import Database


class CustomerAnalysis:
    """
    Performs customer analytics for IntelliBiz.
    Provides customer behavior and value insights.
    """

    def __init__(self):
        self.db = Database()

    def get_total_customers(self, company_id):
        """
        Returns total number of customers.
        """

        query = f"""
        SELECT COUNT(*) AS total_customers
        FROM customers where company_id = {company_id};
        """

        result = self.db.execute_query(query)

        return result
    


    def get_repeat_customer_rate(self, company_id):
        """
        Returns repeat customer statistics.
        """

        query = f"""
        SELECT
            COUNT(*) AS repeat_customers,
            ROUND(
                COUNT(*) * 100.0 /
                (SELECT COUNT(DISTINCT customer_id) FROM sales where company_id = {company_id}),
                2
            ) AS repeat_customer_rate
        FROM (
            SELECT customer_id
            FROM sales where company_id = {company_id}
            GROUP BY customer_id
            HAVING COUNT(*) > 1
        ) AS repeat_buyers;
        """

        return self.db.execute_query(query)
    



    def get_customer_lifetime_value(self, company_id):

        query = f"""
        SELECT
            ROUND(
                SUM(revenue) /
                COUNT(DISTINCT customer_id),
                2
            ) AS customer_lifetime_value
        FROM sales where company_id = {company_id};
        """

        return self.db.execute_query(query)
    


    def get_customer_purchase_frequency(self, company_id):

        query = f"""
        SELECT
            ROUND(
                COUNT(*) /
                COUNT(DISTINCT customer_id),
                2
            ) AS purchase_frequency
        FROM sales where company_id = {company_id};
        """

        return self.db.execute_query(query)
    




    def get_customer_regions(self, company_id, limit=10):
        """
        Returns top customer regions.
        """

        query = f"""
        SELECT
            c.state,
            c.city,
            COUNT(DISTINCT c.customer_id) AS total_customers
        FROM customers c where company_id = {company_id}
        GROUP BY c.state, c.city
        ORDER BY total_customers DESC
        LIMIT {limit};
        """

        return self.db.execute_query(query)
    


