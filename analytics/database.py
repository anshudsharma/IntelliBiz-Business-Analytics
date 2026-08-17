from sqlalchemy import create_engine, text
import pandas as pd

from utils.config import Config


class Database:
    """
    Database service for IntelliBiz Analytics Engine.
    Handles MySQL/TiDB connections and SQL query execution.
    """

    def __init__(self):
        """
        Initialize database connection to TiDB Cloud.
        """

        connection_string = (
            f"mysql+pymysql://"
            f"3Wfwxj99pLxkSmM.root:"
            f"{Config.DB_PASSWORD}@"
            f"gateway01.ap-southeast-1.prod.aws.tidbcloud.com:"
            f"4000/sys"
        )

        self.engine = create_engine(
            connection_string,
            connect_args={
                "ssl": {
                    "ca": "/etc/ssl/certs/ca-certificates.crt"
                }
            },
            pool_pre_ping=True
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
