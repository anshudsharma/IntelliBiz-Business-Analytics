import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Central configuration class for IntelliBiz.
    All application settings should be accessed from here.
    """

    # MySQL Database Configuration
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")