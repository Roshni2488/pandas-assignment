import pandas as pd

# SESSION 10: MERGING & JOINING DATAFRAMES


# TASK 1: Users + Orders - Inner Join
users = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "username": ["Riya", "Amit", "Neha", "Rahul", "Pooja"],
    "city": ["Delhi", "Mumbai", "Pune", "Ahmedabad", "Jaipur"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107],
    "user_id": [1, 2, 2, 3, 4, 1, 3],
    "order_amount": [500, 700, 300, 900, 450, 600, 800]
})

result = pd.merge(users, orders, on="user_id", how="inner")

print("TASK 1 - Inner Join")
print(result)


# TASK 2: Users + Orders - Left Join
result = pd.merge(users, orders, on="user_id", how="left")

print("\nTASK 2 - Left Join")
print(result)


# TASK 3: Restaurants + Reviews - Outer Join
restaurants = pd.DataFrame({
    "restaurant_id": [1, 2, 3, 4],
    "name": ["A", "B", "C", "D"],
    "city": ["Delhi", "Mumbai", "Pune", "Ahmedabad"]
})

reviews = pd.DataFrame({
    "review_id": [101, 102, 103, 104],
    "restaurant_id": [1, 2, 3, 5],
    "rating": [5, 4, 3, 5],
    "reviewer_city": ["Delhi", "Mumbai", "Pune", "Jaipur"]
})

result = pd.merge(
    restaurants,
    reviews,
    on="restaurant_id",
    how="outer"
)

print("\nTASK 3 - Outer Join")
print(result)


# TASK 4: Playlists + User Profiles - Multiple Keys
playlists = pd.DataFrame({
    "playlist_id": [1, 2, 3, 4],
    "user_id": [101, 102, 103, 104],
    "genre": ["Pop", "Rock", "Jazz", "Hip-Hop"]
})

user_profiles = pd.DataFrame({
    "user_id": [101, 102, 103, 105],
    "username": ["Riya", "Amit", "Neha", "Rahul"],
    "city": ["Delhi", "Mumbai", "Pune", "Jaipur"]
})

# Add city to playlists for multiple-key join
playlists["city"] = ["Delhi", "Mumbai", "Pune", "Ahmedabad"]

result = pd.merge(
    playlists,
    user_profiles,
    on=["user_id", "city"],
    how="inner"
)

print("\nTASK 4 - Multiple Key Join")
print(result)


# TASK 5: Flipkart Products + Ratings - Right Join
products = pd.DataFrame({
    "product_id": [1, 2, 3],
    "name": ["Phone", "Laptop", "Headphones"],
    "category": ["Electronics", "Electronics", "Accessories"]
})

ratings = pd.DataFrame({
    "rating_id": [101, 102, 103, 104],
    "product_id": [1, 2, 3, 4],
    "rating": [5, 4, 5, 3]
})

result = pd.merge(
    products,
    ratings,
    on="product_id",
    how="right"
)

print("\nTASK 5 - Right Join")
print(result)