from analytics.business_metrics import BusinessMetrics

metrics = BusinessMetrics()

print("\n===== REVENUE PER CUSTOMER =====")
print(metrics.get_revenue_per_customer())

print("\n===== PROFIT PER CUSTOMER =====")
print(metrics.get_profit_per_customer())


print("\n===== REVENUE PER PRODUCT =====")
print(metrics.get_revenue_per_product())

print("\n===== PROFIT PER PRODUCT =====")
print(metrics.get_profit_per_product())

print("\n===== CUSTOMER RETENTION INDEX =====")
print(metrics.get_customer_retention_index())