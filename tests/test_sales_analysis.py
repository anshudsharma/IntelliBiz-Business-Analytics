from analytics.sales_analysis import SalesAnalysis


def test_sales_analysis():
    """
    Test IntelliBiz sales analytics.
    """

    sales = SalesAnalysis()

    company_id = 1

    top_products = sales.get_top_selling_products(company_id)
    top_revenue_products = sales.get_top_revenue_products(company_id)
    most_profitable_products = sales.get_most_profitable_products(company_id)
    sales_by_category = sales.get_sales_by_category(company_id)
    sales_by_payment = sales.get_sales_by_payment_method(company_id)
    monthly_sales = sales.get_monthly_sales(company_id)
    sales_by_region = sales.get_sales_by_region(company_id)






    print("\n===== TOP SELLING PRODUCTS =====")
    print(top_products)
    print("\n===== TOP REVENUE PRODUCTS =====")
    print(top_revenue_products)
    print("\n===== MOST PROFITABLE PRODUCTS =====")
    print(most_profitable_products)
    print("\n===== SALES BY CATEGORY =====")
    print(sales_by_category.to_string())
    print("\n===== SALES BY PAYMENT METHOD =====")
    print(sales_by_payment.to_string())
    print("\n===== MONTHLY SALES ANALYSIS =====")
    print(monthly_sales.to_string())
    print("\n===== SALES BY REGION =====")
    print(sales_by_region.to_string())





if __name__ == "__main__":
    test_sales_analysis()




