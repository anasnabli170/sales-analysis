import matplotlib.pyplot as plt
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGION_CHART_PATH = os.path.join(BASE_PATH, "outputs", "region-chart.png")
PRODUCT_CHART_PATH = os.path.join(BASE_PATH, "outputs", "product-chart.png")
CUSTOMER_CHART_PATH = os.path.join(BASE_PATH, "outputs", "customer-chart.png")
MONTH_CHART_PATH = os.path.join(BASE_PATH, "outputs", "month-chart.png")
MONTH_PLOT_PATH = os.path.join(BASE_PATH, "outputs", "month-plot.png")


def create_region_bar(revenue_by_region):
    plt.figure(figsize=(10, 6))
    plt.bar(revenue_by_region.index, revenue_by_region.values, color="green")
    plt.title("Total Revenue per Region")
    plt.xlabel("Region")
    plt.ylabel("Total revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(REGION_CHART_PATH)
    plt.show()


def create_product_bar(revenue_by_product):
    plt.figure(figsize=(10, 6))
    plt.bar(revenue_by_product.index, revenue_by_product.values, color="orange")
    plt.title("Total Revenue per Product")
    plt.xlabel("Product")
    plt.ylabel("Total revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(PRODUCT_CHART_PATH)
    plt.show()


def create_customer_bar(revenue_by_customer):
    plt.figure(figsize=(10, 6))
    plt.bar(revenue_by_customer.index, revenue_by_customer.values, color="pink")
    plt.title("Total Revenue per Customer")
    plt.xlabel("Customer")
    plt.ylabel("Total revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(CUSTOMER_CHART_PATH)
    plt.show()


def create_month_bar(revenue_by_month):
    plt.figure(figsize=(10, 6))
    plt.bar(revenue_by_month.index, revenue_by_month.values)
    plt.title("Total Revenue per Month")
    plt.xlabel("Month")
    plt.ylabel("Total revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(MONTH_CHART_PATH)
    plt.show()


def create_month_plot(revenue_by_month):
    plt.figure(figsize=(10, 6))
    plt.plot(revenue_by_month.index, revenue_by_month.values, "r-o")
    plt.title("Total Revenue per Month")
    plt.xlabel("Month")
    plt.ylabel("Total revenue ($)")
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    plt.xticks(ticks=range(1, 13), labels=month_names, rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.savefig(MONTH_PLOT_PATH)
    plt.show()
