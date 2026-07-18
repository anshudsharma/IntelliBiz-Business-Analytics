from analytics.database import Database


class ProductAnalysis:
    """
    Performs product analytics for IntelliBiz.
    """

    def __init__(self):
        self.db = Database()



    def get_total_products(self, company_id):
        """
        Returns total number of products.
        """

        query = f"""
        SELECT COUNT(*) AS total_products
        FROM products WHERE company_id = {company_id};
        """

        return self.db.execute_query(query, company_id)
    

    def get_product_categories(self, company_id):
        """
        Returns total product categories.
        """

        query = f"""
        SELECT COUNT(DISTINCT category) AS total_categories
        FROM products WHERE company_id = {company_id};
        """

        return self.db.execute_query(query, company_id)
    



    def get_average_product_price(self, company_id):
        """
        Returns average selling price.
        """

        query = f"""
        SELECT
            ROUND(AVG(selling_price), 2) AS average_product_price
        FROM sales WHERE company_id = {company_id};
        """

        return self.db.execute_query(query)
    



    def get_category_performance(self, company_id, limit=10):
        """
        Returns top performing product categories by revenue.
        """

        query = f"""
        SELECT
            p.category,
            SUM(s.revenue) AS total_revenue
        FROM sales s
        JOIN products p
            ON s.product_id = p.product_id  WHERE company_id = {company_id}
        GROUP BY p.category
        ORDER BY total_revenue DESC
        LIMIT {limit};
        """

        return self.db.execute_query(query)
    





    def get_category_profitability(self, company_id, limit=10):
        """
        Returns most profitable product categories.
        """

        query = f"""
        SELECT
            p.category,
            SUM(s.profit) AS total_profit
        FROM sales s
        JOIN products p
            ON s.product_id = p.product_id  WHERE company_id = {company_id}
        GROUP BY p.category
        ORDER BY total_profit DESC
        LIMIT {limit};
        """

        return self.db.execute_query(query)
    


