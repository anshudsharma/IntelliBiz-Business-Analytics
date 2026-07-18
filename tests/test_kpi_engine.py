from analytics.kpi_engine import KPIEngine


def test_kpis():
    """
    Test IntelliBiz KPI calculations.
    """

    kpi = KPIEngine()

    company_id = 1

    revenue = kpi.get_total_revenue(company_id)
    profit = kpi.get_total_profit(company_id)
    orders = kpi.get_total_orders(company_id)
    aov = kpi.get_average_order_value(company_id)
    profit_margin = kpi.get_profit_margin(company_id)
    monthly_revenue = kpi.get_monthly_revenue(company_id)
    revenue_growth = kpi.get_revenue_growth(company_id)
    monthly_profit = kpi.get_monthly_profit(company_id)
    profit_growth = kpi.get_profit_growth(company_id)
    


    print("\n===== INTELLIBIZ KPI REPORT =====")
    print(f"Company ID: {company_id}")
    print(f"Total Revenue: ${revenue:,.2f}")
    
    print(f"Total Profit: ${profit:,.2f}")
    print(f"Total Orders: {orders:,}")
    print(f"Average Order Value: ${aov:,.2f}")
    print(f"Profit Margin: {profit_margin}%")
    print("\n===== MONTHLY REVENUE TREND =====")
    print(monthly_revenue)
    print("\n===== REVENUE GROWTH TREND =====")
    print(revenue_growth)
    print("\n===== MONTHLY PROFIT TREND =====")
    print(monthly_profit)
    print("\n===== PROFIT GROWTH TREND =====")
    print(profit_growth)


if __name__ == "__main__":
    test_kpis()