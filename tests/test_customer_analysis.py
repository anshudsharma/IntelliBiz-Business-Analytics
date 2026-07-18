from analytics.customer_analysis import CustomerAnalysis


customer = CustomerAnalysis()


print("\n===== TOTAL CUSTOMERS =====")
print(customer.get_total_customers())

print("\n===== REPEAT CUSTOMER RATE =====")
print(customer.get_repeat_customer_rate())


print("\n===== CUSTOMER LIFETIME VALUE  =====")
print(customer.get_customer_lifetime_value())

print("\n===== PURCHASE FREQUENCY =====")
print(customer.get_customer_purchase_frequency())

print("\n===== CUSTOMER REGIONS =====")
print(customer.get_customer_regions())