import pandas as pd

# SESSION 11: CONCATENATION & DATA RESHAPING


# TASK 1: Swiggy Orders - Row-wise Concatenation
jan = pd.DataFrame({
    "order_id": [1, 2, 3],
    "customer": ["Riya", "Amit", "Neha"],
    "amount": [300, 450, 250]
})

feb = pd.DataFrame({
    "order_id": [4, 5, 6],
    "customer": ["Rahul", "Pooja", "Karan"],
    "amount": [500, 350, 400]
})

result = pd.concat([jan, feb], ignore_index=True)

print("TASK 1 - Swiggy Orders")
print(result)


# TASK 2: Flipkart Products - Column-wise Concatenation
products = pd.DataFrame({
    "product_id": [1, 2, 3],
    "product": ["Phone", "Laptop", "Mouse"]
})

ratings = pd.DataFrame({
    "rating": [5, 4, 5]
})

result = pd.concat([products, ratings], axis=1)

print("\nTASK 2 - Flipkart Products & Ratings")
print(result)


# TASK 3: Spotify - Pivot
df = pd.DataFrame({
    "user": ["Riya", "Riya", "Amit", "Amit", "Neha", "Neha"],
    "day": ["Mon", "Tue", "Mon", "Tue", "Mon", "Tue"],
    "streams": [100, 150, 200, 250, 120, 180]
})

result = df.pivot(
    index="user",
    columns="day",
    values="streams"
)

print("\nTASK 3 - Spotify Daily Streams")
print(result)


# TASK 4: Zomato - Pivot Table
df = pd.DataFrame({
    "restaurant": ["A", "A", "B", "B", "C", "C"],
    "month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "total_amount": [300, 400, 500, 600, 250, 350]
})

result = pd.pivot_table(
    df,
    index="restaurant",
    columns="month",
    values="total_amount",
    aggfunc="mean"
)

print("\nTASK 4 - Zomato Average Order Amount")
print(result)


# TASK 5: Myntra - Concatenate Monthly Sales & Total by Product
jan = pd.DataFrame({
    "product": ["Shirt", "Shoes"],
    "sales": [1000, 2000]
})

feb = pd.DataFrame({
    "product": ["Shirt", "Shoes"],
    "sales": [1500, 2500]
})

mar = pd.DataFrame({
    "product": ["Shirt", "Shoes"],
    "sales": [1200, 3000]
})

sales = pd.concat([jan, feb, mar], ignore_index=True)

result = sales.groupby("product")["sales"].sum()

print("\nTASK 5 - Myntra Total Sales")
print(result)