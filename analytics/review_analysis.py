from analytics.database import Database


class ReviewAnalysis:
    """
    Performs review analytics for IntelliBiz.
    """

    def __init__(self):
        self.db = Database()



    def get_average_review_score(self, company_id):
        """
        Returns average customer review rating.
        """

        query = f"""
        SELECT
            ROUND(AVG(rating), 2) AS average_review_score
        FROM reviews WHERE company_id = {company_id};
        """

        return self.db.execute_query(query, company_id)
    



    def get_review_distribution(self, company_id):
        """
        Returns review rating distribution.
        """

        query = f"""
        SELECT
            rating,
            COUNT(*) AS total_reviews
        FROM reviews WHERE company_id = {company_id}
        GROUP BY rating
        ORDER BY rating;
        """

        return self.db.execute_query(query)
    


    def get_best_rated_categories(self, company_id, limit=10):
        """
        Returns highest rated product categories.
        """

        query = f"""
        SELECT
            p.category,
            ROUND(AVG(r.rating), 2) AS average_rating,
            COUNT(*) AS total_reviews
        FROM reviews r
        JOIN sales s
            ON r.order_id = s.order_id
        JOIN products p
            ON s.product_id = p.product_id  WHERE company_id = {company_id}
        GROUP BY p.category
        HAVING COUNT(*) >= 50
        ORDER BY average_rating DESC
        LIMIT {limit};
        """

        return self.db.execute_query(query)
    



    def get_worst_rated_categories(self, company_id, limit=10):
        """
        Returns lowest rated product categories.
        """

        query = f"""
        SELECT
            p.category,
            ROUND(AVG(r.rating), 2) AS average_rating,
            COUNT(*) AS total_reviews
        FROM reviews r
        JOIN sales s
            ON r.order_id = s.order_id
        JOIN products p
            ON s.product_id = p.product_id  WHERE company_id = {company_id}
        GROUP BY p.category
        HAVING COUNT(*) >= 50
        ORDER BY average_rating ASC
        LIMIT {limit};
        """

        return self.db.execute_query(query)
    

