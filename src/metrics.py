def calculate_total_revenue(df):
    df = df.copy()
    df["total_revenue"] = df["quantity"] * df["unit_price"]
    return df


def best_region(df):
    revenue_by_region = df.groupby("region")["total_revenue"].sum()
    revenue_by_region = revenue_by_region.sort_values(ascending=False)
    region = revenue_by_region.index[0]
    amount = revenue_by_region.iloc[0]
    return revenue_by_region, region, amount


def best_product(df):
    revenue_by_product = df.groupby("product")["total_revenue"].sum()
    revenue_by_product = revenue_by_product.sort_values(ascending=False)
    product = revenue_by_product.index[0]
    amount = revenue_by_product.iloc[0]
    return revenue_by_product, product, amount


def best_customer(df):
    revenue_by_customer = df.groupby("customer_id")["total_revenue"].sum()
    revenue_by_customer = revenue_by_customer.sort_values(ascending=False)
    customer = revenue_by_customer.index[0]
    amount = revenue_by_customer.iloc[0]
    return revenue_by_customer, customer, amount


def best_month(df):
    df["month"] = df["date"].dt.month_name()
    df["month_number"] = df["date"].dt.month
    revenue_by_month = df.groupby("month")["total_revenue"].sum()
    revenue_by_month = revenue_by_month.sort_values(ascending=False)
    revenue_by_month_number = df.groupby("month_number")["total_revenue"].sum()

    month = revenue_by_month.index[0]
    amount = revenue_by_month.iloc[0]
    return revenue_by_month_number, revenue_by_month, month, amount
