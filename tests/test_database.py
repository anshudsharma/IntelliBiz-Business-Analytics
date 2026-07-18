from analytics.database import Database


def test_database_connection():
    """
    Test IntelliBiz analytics database connection.
    """

    db = Database()

    db.test_connection()


if __name__ == "__main__":
    test_database_connection()