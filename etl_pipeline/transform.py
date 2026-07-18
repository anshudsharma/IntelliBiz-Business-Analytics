"""
transform.py

Purpose:
    Converts raw Olist datasets into IntelliBiz
    business-ready tables.

Transformations include:
    - Customer transformation
    - Product transformation
    - Order transformation
    - Sales fact table creation
    - Review transformation
    - Inventory transformation

Future enhancements:
    - Advanced data cleaning
    - Additional business rules
    - Data enrichment
"""

import pandas as pd

def transform_customers(customers_df, company_id):
    """
    Transform customer data into IntelliBiz customer format.
    """

    print("\nTransforming customers data...")

    # Create a copy to avoid modifying original data
    customers = customers_df.copy()


    # Rename columns to match database schema
    customers = customers.rename(columns={
        "customer_zip_code_prefix": "zip_code",
        "customer_city": "city",
        "customer_state": "state"
    })


    # Add multi-tenant company isolation
    customers["company_id"] = company_id


    # Select only required columns
    customers = customers[
        [
            "customer_id",
            "company_id",
            "zip_code",
            "city",
            "state"
        ]
    ]


    print(
        f"Customers transformation completed. "
        f"Shape: {customers.shape}"
    )


    return customers

def transform_products(products_df, category_df, company_id):
    """
    Transform product data into IntelliBiz product format.
    """

    print("\nTransforming products data...")

    # Create copies to preserve original datasets
    products = products_df.copy()
    categories = category_df.copy()

    # Merge products with category translation
    products = products.merge(
        categories,
        on="product_category_name",
        how="left"
    )

    # Rename columns according to database schema
    products = products.rename(columns={
        "product_category_name_english": "category",
        "product_weight_g": "weight",
        "product_length_cm": "length",
        "product_height_cm": "height",
        "product_width_cm": "width"
    })

    # Add company ID for multi-tenant isolation
    products["company_id"] = company_id

    # Handle missing categories
    products["category"] = products["category"].fillna(
        "Unknown"
    )

    # Select required columns
    products = products[
        [
            "product_id",
            "company_id",
            "category",
            "weight",
            "length",
            "height",
            "width"
        ]
    ]

    print(
        f"Products transformation completed. "
        f"Shape: {products.shape}"
    )

    return products


def transform_orders(orders_df, company_id):
    """
    Transform order data into IntelliBiz order format.
    """

    print("\nTransforming orders data...")

    # Create copy to protect original dataset
    orders = orders_df.copy()


    # Convert timestamp columns to datetime format
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for column in date_columns:
        orders[column] = pd.to_datetime(
            orders[column],
            errors="coerce"
        )


    # Rename columns according to database schema
    orders = orders.rename(columns={
        "order_status": "status",
        "order_purchase_timestamp": "purchase_date",
        "order_approved_at": "approved_date",
        "order_delivered_customer_date": "delivered_date",
        "order_estimated_delivery_date": "estimated_delivery_date"
    })


    # Add company ID for multi-tenant isolation
    orders["company_id"] = company_id


    # Select required columns
    orders = orders[
        [
            "order_id",
            "company_id",
            "customer_id",
            "status",
            "purchase_date",
            "approved_date",
            "delivered_date",
            "estimated_delivery_date"
        ]
    ]


    print(
        f"Orders transformation completed. "
        f"Shape: {orders.shape}"
    )


    return orders




def create_sales_table(orders_df, order_items_df, payments_df, company_id):
    """
    Create the sales fact table for IntelliBiz.
    """

    print("\nCreating sales table...")

    # Create copies of datasets
    orders = orders_df.copy()
    items = order_items_df.copy()
    payments = payments_df.copy()

    # Aggregate payment information per order
    payments = (
        payments
        .groupby("order_id")
        .agg({
            "payment_type": "first",
            "payment_value": "sum"
        })
        .reset_index()
    )

    # Merge orders with order items
    sales = orders.merge(
        items,
        on="order_id",
        how="inner"
    )

    # Merge payment information
    sales = sales.merge(
        payments,
        on="order_id",
        how="left"
    )

    # Add company ID for multi-tenant architecture
    sales["company_id"] = company_id

    # Olist does not provide quantity
    sales["quantity"] = 1

    # Rename columns according to sales table schema
    sales = sales.rename(columns={
        "purchase_date": "sale_date",
        "price": "selling_price",
        "freight_value": "shipping_cost",
        "payment_type": "payment_method"
    })

    # Calculate revenue
    sales["revenue"] = (
        sales["selling_price"] * sales["quantity"]
    )

    # Estimated cost (70% of revenue)
    sales["estimated_cost"] = (
        sales["revenue"] * 0.70
    )

    # Estimated profit
    sales["profit"] = (
        sales["revenue"] - sales["estimated_cost"]
    )

    # Generate unique sale IDs
    sales["sale_id"] = range(1, len(sales) + 1)

    # Select final columns
    sales = sales[
        [
            "sale_id",
            "company_id",
            "order_id",
            "customer_id",
            "product_id",
            "sale_date",
            "quantity",
            "selling_price",
            "shipping_cost",
            "payment_method",
            "revenue",
            "estimated_cost",
            "profit"
        ]
    ]

    print(
        f"Sales table created successfully. "
        f"Shape: {sales.shape}"
    )

    return sales






def transform_reviews(reviews_df, company_id):
    """
    Transform review data into IntelliBiz review format.
    """

    print("\nTransforming reviews data...")

    # Create copy to preserve original dataset
    reviews = reviews_df.copy()


    # Convert review date to datetime
    reviews["review_creation_date"] = pd.to_datetime(
        reviews["review_creation_date"],
        errors="coerce"
    )


    # Rename columns according to database schema
    reviews = reviews.rename(columns={
        "review_score": "rating",
        "review_creation_date": "review_date",
        "review_comment_message": "comment"
    })


    # Add company ID for multi-tenant isolation
    reviews["company_id"] = company_id


    # Handle missing comments
    reviews["comment"] = reviews["comment"].fillna(
        "No comment provided"
    )


    # Select required columns
    reviews = reviews[
        [
            "review_id",
            "company_id",
            "order_id",
            "rating",
            "review_date",
            "comment"
        ]
    ]


    print(
        f"Reviews transformation completed. "
        f"Shape: {reviews.shape}"
    )


    return reviews





def transform_data(dataframes, company_id):
    """
    Main transformation controller for IntelliBiz ETL.
    Executes all transformation functions and returns
    clean business-ready datasets.
    """

    print("\n=================================")
    print(" Starting Data Transformation")
    print("=================================\n")


    # Transform customers
    customers = transform_customers(
        dataframes["customers"],
        company_id
    )


    # Transform products and translate categories
    products = transform_products(
        dataframes["products"],
        dataframes["category_translation"],
        company_id
    )


    # Transform orders
    orders = transform_orders(
        dataframes["orders"],
        company_id
    )


    # Create sales fact table
    sales = create_sales_table(
        orders,
        dataframes["order_items"],
        dataframes["payments"],
        company_id
    )


    # Transform customer reviews
    reviews = transform_reviews(
        dataframes["reviews"],
        company_id
    )


    print("\n=================================")
    print(" Data Transformation Completed")
    print("=================================\n")


    # Return all transformed datasets
    transformed_data = {
        "customers": customers,
        "products": products,
        "orders": orders,
        "sales": sales,
        "reviews": reviews
    }


    return transformed_data