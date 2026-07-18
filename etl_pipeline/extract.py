import pandas as pd
import os


# Path to raw datasets folder
DATA_PATH = os.path.join("datasets", "raw")


def extract_data():
    """
    Extract all raw datasets and return them as pandas DataFrames.
    """

    datasets = {
        "customers": "olist_customers_dataset.csv",
        "orders": "olist_orders_dataset.csv",
        "products": "olist_products_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "payments": "olist_order_payments_dataset.csv",
        "reviews": "olist_order_reviews_dataset.csv",
        "category_translation": "product_category_name_translation.csv"
    }

    dataframes = {}

    for name, filename in datasets.items():

        file_path = os.path.join(DATA_PATH, filename)

        print(f"Loading {filename}...")

        df = pd.read_csv(file_path)

        dataframes[name] = df

        print(f"{name} loaded successfully. Shape: {df.shape}")

    return dataframes