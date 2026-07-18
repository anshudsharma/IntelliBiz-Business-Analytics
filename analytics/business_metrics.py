from analytics.database import Database


class BusinessMetrics:
    """
    Calculates advanced business metrics for IntelliBiz.
    """

    def __init__(self):
        self.db = Database()

    def get_revenue_per_customer(self, company_id):
        """
        Returns average revenue per customer.
        """

        query = f"""
        SELECT
            ROUND(
                SUM(revenue) /
                COUNT(DISTINCT customer_id),
                2
            ) AS revenue_per_customer
        FROM sales WHERE company_id = {company_id};
        """

        return self.db.execute_query(query)
    


    def get_profit_per_customer(self, company_id):
        """
        Returns average profit generated per customer.
        """

        query = f"""
        SELECT
            ROUND(
                SUM(profit) /
                COUNT(DISTINCT customer_id),
                2
            ) AS profit_per_customer
        FROM sales WHERE company_id = {company_id};
        """

        return self.db.execute_query(query)
    


    def get_revenue_per_product(self, company_id):
        """
        Returns average revenue generated per product.
        """

        query = """
        SELECT
            ROUND(
                SUM(revenue) /
                COUNT(DISTINCT product_id),
                2
            ) AS revenue_per_product
        FROM sales WHERE company_id = {company_id};
        """

        return self.db.execute_query(query)
    


    def get_profit_per_product(self, company_id):
        """
        Returns average profit generated per product.
        """

        query = """
        SELECT
            ROUND(
                SUM(profit) /
                COUNT(DISTINCT product_id),
                2
            ) AS profit_per_product
        FROM sales WHERE company_id = {company_id};
        """

        return self.db.execute_query(query)
    


    def get_customer_retention_index(self, company_id):
        """
        Returns customer retention percentage.
        """

        query = """
        SELECT
            ROUND(
                COUNT(*) * 100.0 /
                (SELECT COUNT(DISTINCT customer_id) FROM sales WHERE company_id = {company_id}),
                2
            ) AS retention_index
        FROM (
            SELECT customer_id
            FROM sales WHERE company_id = {company_id}
            GROUP BY customer_id
            HAVING COUNT(*) > 1
        ) AS repeat_customers;
        """

        return self.db.execute_query(query)
    