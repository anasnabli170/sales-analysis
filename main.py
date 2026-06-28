from src.loader import load_data
from src.metrics import (
    calculate_total_revenue,
    best_region,
    best_product,
    best_customer,
    best_month,
)
from src.visualizer import (
    create_region_bar,
    create_product_bar,
    create_customer_bar,
    create_month_bar,
    create_month_plot,
)

df = load_data()
df = calculate_total_revenue(df)
revenue_by_region, best_region_name, best_region_amount = best_region(df)
revenue_by_product, best_product_name, best_product_amount = best_product(df)
revenue_by_customer, best_customer_name, best_customer_amount = best_customer(df)
(
    revenue_by_month_number,
    revenue_by_month,
    best_month_name,
    best_month_amount,
) = best_month(df)

print(revenue_by_region)
print(
    f"The region with the top total revenue is: {best_region_name} with {best_region_amount}$"
)

print(revenue_by_product)
print(
    f"The product with the top total revenue is: {best_product_name} with {best_product_amount}"
)

print(revenue_by_customer)
print(
    f"The customer with the top total revenue is: {best_customer_name} with {best_customer_amount}"
)

print(revenue_by_month)
print(
    f"The month with the top total revenue is: {best_month_name} with {best_month_amount}"
)
create_region_bar(revenue_by_region)
create_product_bar(revenue_by_product)
create_customer_bar(revenue_by_customer[:10])
create_month_bar(revenue_by_month)
create_month_plot(revenue_by_month_number)
