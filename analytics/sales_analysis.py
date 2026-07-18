from analytics.database import Database


class SalesAnalysis:
    """
    Performs detailed sales analytics for IntelliBiz.
    """

    def __init__(self):
        """
        Initialize database service.
        """
        self.db = Database()





    def get_top_selling_products(self, company_id, limit=10):
        """
        Get the top selling products by quantity.
        """

        query = """
        SELECT
            product_id,
            SUM(quantity) AS total_quantity_sold
        FROM sales
        WHERE company_id = :company_id
        GROUP BY product_id
        ORDER BY total_quantity_sold DESC
        LIMIT :limit;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id,
                "limit": limit
            }
        )

        return result      
    



    def get_top_revenue_products(self, company_id, limit=10):
        """
        Get products generating the highest revenue.
        """

        query = """
        SELECT
            product_id,
            ROUND(SUM(revenue), 2) AS total_revenue
        FROM sales
        WHERE company_id = :company_id
        GROUP BY product_id
        ORDER BY total_revenue DESC
        LIMIT :limit;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id,
                "limit": limit
            }
        )

        return result
    


    def get_most_profitable_products(self, company_id, limit=10):
        """
        Get products generating the highest profit.
        """

        query = """
        SELECT
            product_id,
            ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        WHERE company_id = :company_id
        GROUP BY product_id
        ORDER BY total_profit DESC
        LIMIT :limit;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id,
                "limit": limit
            }
        )

        return result
    

    def get_sales_by_category(self, company_id):
        """
        Analyze sales performance by product category.
        """

        query = """
        SELECT
            p.category,
            ROUND(SUM(s.revenue), 2) AS total_revenue,
            ROUND(SUM(s.profit), 2) AS total_profit,
            SUM(s.quantity) AS total_quantity_sold
        FROM sales s
        JOIN products p
            ON s.product_id = p.product_id
        WHERE s.company_id = :company_id
        GROUP BY p.category
        ORDER BY total_revenue DESC;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id
            }
        )

        return result
    



    def get_sales_by_payment_method(self, company_id):
        """
        Analyze sales performance by payment method.
        """

        query = """
        SELECT
            payment_method,
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(SUM(revenue), 2) AS total_revenue,
            ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        WHERE company_id = :company_id
        GROUP BY payment_method
        ORDER BY total_revenue DESC;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id
            }
        )

        return result
    

    def get_monthly_sales(self, company_id):
        """
        Analyze monthly order volume.
        """

        query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            COUNT(DISTINCT order_id) AS total_orders,
            SUM(quantity) AS total_items_sold
        FROM sales
        WHERE company_id = :company_id
        GROUP BY month
        ORDER BY month;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id
            }
        )

        return result
    



    def get_sales_by_region(self, company_id, limit=10):
        """
        Analyze sales performance by customer region.
        """

        query = """
        SELECT
            c.state,
            c.city,
            COUNT(DISTINCT s.order_id) AS total_orders,
            ROUND(SUM(s.revenue), 2) AS total_revenue,
            ROUND(SUM(s.profit), 2) AS total_profit
        FROM sales s
        JOIN customers c
            ON s.customer_id = c.customer_id
        WHERE s.company_id = :company_id
        GROUP BY c.state, c.city
        ORDER BY total_revenue DESC LIMIT :limit;
        """

        result = self.db.execute_query(
            query,
            {
                "company_id": company_id, "limit": limit
            }
        )

        return result