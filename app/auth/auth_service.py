from analytics.database import Database


class AuthService:

    def __init__(self):

        self.db = Database()


    def login(
        self,
        email,
        password
    ):

        query = """
        SELECT *
        FROM users
        WHERE email = :email
        AND password_hash = :password
        """

        result = self.db.execute_query(
            query,
            {
                "email": email,
                "password": password
            }
        )

        if result.empty:

            return None

        return result.iloc[0]