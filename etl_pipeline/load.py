"""
load.py

Purpose:
    Loads transformed IntelliBiz data into MySQL Data Warehouse.

Functions:
    - create_database_engine()
    - load individual business tables
    - load complete transformed datasets
"""

from sqlalchemy import create_engine



# Step 1: Add imports and create create_database_engine()
def create_database_engine():
    """
    Creates SQLAlchemy engine for MySQL connection.
    """

    print("\nConnecting to IntelliBiz Database...")


    # Database credentials
    username = "root"
    password = "1234"
    host = "localhost"
    port = 3306
    database = "intellibiz_db"


    # SQLAlchemy connection string
    connection_url = (
        f"mysql+pymysql://{username}:{password}"
        f"@{host}:{port}/{database}"
    )


    # Create database engine
    engine = create_engine(connection_url)


    print("Database connection successful!")

    return engine




#Step 2: Create load_customers()
#Now we will write our first real loading function.
def load_customers(customers_df, engine):
    """
    Load customer data into MySQL customers table.
    """

    print("\nLoading customers into database...")


    customers_df.to_sql(
        name="customers",
        con=engine,
        if_exists="append",
        index=False
    )


    print(
        f"Customers loaded successfully. "
        f"Rows inserted: {len(customers_df)}"
    )



# Step 3: Create load_products()
# This function will take our transformed products DataFrame and insert it into the MySQL products table.
def load_products(products_df, engine):
    """
    Load product data into MySQL products table.
    """

    print("\nLoading products into database...")


    products_df.to_sql(
        name="products",
        con=engine,
        if_exists="append",
        index=False
    )


    print(
        f"Products loaded successfully. "
        f"Rows inserted: {len(products_df)}"
    )



#Step 4: Create load_orders()
#This function will take our transformed orders DataFrame and insert it into the MySQL orders table.
def load_orders(orders_df, engine):
    """
    Load order data into MySQL orders table.
    """

    print("\nLoading orders into database...")


    orders_df.to_sql(
        name="orders",
        con=engine,
        if_exists="append",
        index=False
    )


    print(
        f"Orders loaded successfully. "
        f"Rows inserted: {len(orders_df)}"
    )



#Step 5: Create load_sales()
#This is the most important loading function because the sales table is the heart of the IntelliBiz Data Warehouse.
def load_sales(sales_df, engine):
    """
    Load sales fact table into MySQL sales table.
    """

    print("\nLoading sales data into database...")


    sales_df.to_sql(
        name="sales",
        con=engine,
        if_exists="append",
        index=False
    )


    print(
        f"Sales loaded successfully. "
        f"Rows inserted: {len(sales_df)}"
    )



#Step 6: Create load_reviews()
#This function will load our transformed reviews data into the MySQL reviews table.
def load_reviews(reviews_df, engine):
    """
    Load customer review data into MySQL reviews table.
    """

    print("\nLoading reviews into database...")


    reviews_df.to_sql(
        name="reviews",
        con=engine,
        if_exists="append",
        index=False
    )


    print(
        f"Reviews loaded successfully. "
        f"Rows inserted: {len(reviews_df)}"
    )




# Now we will create the manager of the Load layer, just like:
# pipeline.py controls the ETL process
# transform_data() controls all transformations
# load_data() will control all database loading.
def load_data(transformed_data):
    """
    Main loading controller for IntelliBiz ETL.
    Loads all transformed datasets into MySQL.
    """

    print("\n=================================")
    print(" Starting Data Warehouse Loading")
    print("=================================\n")


    # Create database connection
    engine = create_database_engine()


    # Load customers table
    load_customers(
        transformed_data["customers"],
        engine
    )


    # Load products table
    load_products(
        transformed_data["products"],
        engine
    )


    # Load orders table
    load_orders(
        transformed_data["orders"],
        engine
    )


    # Load sales fact table
    load_sales(
        transformed_data["sales"],
        engine
    )


    # Load reviews table
    load_reviews(
        transformed_data["reviews"],
        engine
    )


    print("\n=================================")
    print(" Data Warehouse Loading Completed")
    print("=================================\n")


