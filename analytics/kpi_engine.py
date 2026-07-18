from analytics.database import Database


class KPIEngine:
    """
    Calculates core business KPIs for IntelliBiz.
    """

    def __init__(self):
        """
        Initialize database service.
        """
        self.db = Database()

    def get_total_revenue(self, company_id):
        """
        Calculate total revenue for a company.
        """

        query = """
        SELECT
            ROUND(SUM(revenue), 2) AS total_revenue
        FROM sales
        WHERE company_id = :company_id
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result.iloc[0]["total_revenue"]
    
    def get_total_profit(self, company_id):
        """
        Calculate total profit for a company.
        """

        query = """
        SELECT
            ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        WHERE company_id = :company_id
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result.iloc[0]["total_profit"]
    

    def get_total_orders(self, company_id):
        """
        Calculate total number of orders for a company.
        """

        query = """
        SELECT
            COUNT(DISTINCT order_id) AS total_orders
        FROM orders
        WHERE company_id = :company_id
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result.iloc[0]["total_orders"]
    def get_average_order_value(self, company_id):
        """
        Calculate average revenue per order.
        """

        query = """
        SELECT
            ROUND(
                SUM(revenue) / COUNT(DISTINCT order_id),
                2
            ) AS average_order_value
        FROM sales
        WHERE company_id = :company_id
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result.iloc[0]["average_order_value"]
    

    def get_profit_margin(self, company_id):
        """
        Calculate profit margin percentage.
        """

        query = """
        SELECT
            ROUND(
                (SUM(profit) / SUM(revenue)) * 100,
                2
            ) AS profit_margin
        FROM sales
        WHERE company_id = :company_id
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result.iloc[0]["profit_margin"]
    
    def get_monthly_revenue(self, company_id):
        """
        Calculate monthly revenue trend for a company.
        """

        query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            ROUND(SUM(revenue), 2) AS total_revenue
        FROM sales
        WHERE company_id = :company_id
        GROUP BY month
        ORDER BY month;
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result
    

    def get_revenue_growth(self, company_id):
        """
        Calculate month-over-month revenue growth percentage.
        """

        monthly_revenue = self.get_monthly_revenue(company_id)

        monthly_revenue["growth_percentage"] = (
            monthly_revenue["total_revenue"]
            .pct_change() * 100
        ).round(2)

        return monthly_revenue    
    

    def get_monthly_profit(self, company_id):
        """
        Calculate monthly profit trend for a company.
        """

        query = """
        SELECT
            DATE_FORMAT(sale_date, '%Y-%m') AS month,
            ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        WHERE company_id = :company_id
        GROUP BY month
        ORDER BY month;
        """

        result = self.db.execute_query(
            query,
            {"company_id": company_id}
        )

        return result
    

    def get_profit_growth(self, company_id):
        """
        Calculate month-over-month profit growth percentage.
        """

        monthly_profit = self.get_monthly_profit(company_id)

        monthly_profit["growth_percentage"] = (
            monthly_profit["total_profit"]
            .pct_change() * 100
        ).round(2)

        return monthly_profit
