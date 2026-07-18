from analytics.product_analysis import ProductAnalysis

product = ProductAnalysis()

print("\n===== TOTAL PRODUCTS =====")
print(product.get_total_products())



print("\n===== PRODUCT CATEGORIES =====")
print(product.get_product_categories())



print("\n===== AVERAGE PRODUCT PRICE =====")
print(product.get_average_product_price())

print("\n===== CATEGORY PERFORMANCE =====")
print(product.get_category_performance())

print("\n===== CATEGORY PROFITABILITY =====")
print(product.get_category_profitability())

