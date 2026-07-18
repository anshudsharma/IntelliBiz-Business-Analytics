from sqlalchemy import create_engine, text
import pandas as pd

from utils.config import Config


class Database:
    """
    Database service for IntelliBiz Analytics Engine.
    Handles MySQL connections and SQL query execution.
    """

    def __init__(self):
        """
        Initialize database connection using environment configuration.
        """

        connection_string = (
            f"mysql+pymysql://{Config.DB_USER}:"
            f"{Config.DB_PASSWORD}@{Config.DB_HOST}:"
            f"{Config.DB_PORT}/{Config.DB_NAME}"
        )

        self.engine = create_engine(
            connection_string
        )

    def execute_query(self, query, params=None):
        """
        Execute a SELECT query and return results as a Pandas DataFrame.
        """

        with self.engine.connect() as connection:
            dataframe = pd.read_sql(
                text(query),
                connection,
                params=params
            )

        return dataframe

    def test_connection(self):
        """
        Test whether the database connection is working.
        """

        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            print("Database connection successful!")

        except Exception as error:
            print("Database connection failed!")
            print(error)