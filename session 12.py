import pandas as pd

# SESSION 12: GROUPBY & AGGREGATIONS


# TASK 1: IPL - Total Runs by Team
df = pd.DataFrame({
    "team": ["India", "India", "Australia", "Australia"],
    "runs": [250, 300, 280, 200]
})

print("TASK 1")
print(df.groupby("team")["runs"].sum().to_frame())


# TASK 2: Zomato - Average Order Amount
df = pd.DataFrame({
    "city": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "restaurant": ["A", "A", "B", "B"],
    "order_amount": [200, 300, 400, 500]
})

print("\nTASK 2")
print(df.groupby(["city", "restaurant"])["order_amount"].agg("mean"))


# TASK 3: Flipkart - Multiple Aggregations
df = pd.DataFrame({
    "category": ["Mobile", "Mobile", "Laptop", "Laptop"],
    "region": ["North", "South", "North", "South"],
    "sales": [1000, 2000, 3000, 4000],
    "units_sold": [10, 20, 30, 40]
})

print("\nTASK 3")
print(df.groupby(["category", "region"]).agg(
    total_sales=("sales", "sum"),
    avg_units=("units_sold", "mean")
))


# TASK 4: Revenue - Min & Max by Region
df = pd.DataFrame({
    "region": ["North", "North", "South", "South"],
    "revenue": [1000, 2000, 1500, 3000]
})

print("\nTASK 4")
print(df.groupby("region").agg(
    total=("revenue", "sum"),
    maximum=("revenue", "max"),
    minimum=("revenue", "min")
))


# TASK 5: Spotify - Total & Average Streams
df = pd.DataFrame({
    "artist": ["A", "B", "A", "C"],
    "genre": ["Pop", "Rock", "Pop", "Rock"],
    "streams": [1000, 2000, 3000, 1500]
})

result = df.groupby("genre").agg(
    total_streams=("streams", "sum"),
    average_streams=("streams", "mean")
).sort_values("total_streams", ascending=False)

print("\nTASK 5")
print(result)