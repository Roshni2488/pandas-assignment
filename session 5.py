import pandas as pd

# Task 1: Find Missing Ages





# Task 2: Drop Missing Delivery Ratings

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_name': ['Riya', 'Aman', 'Neha', 'Rahul', 'Priya'],
    'delivery_rating': [4.5, None, 4.0, None, 5.0]
})

orders = orders.dropna(subset=['delivery_rating'])

print(orders)


# Task 3: Fill Missing Ratings with Mean

products = pd.DataFrame({
    'product_name': ['Mobile', 'Laptop', 'Headphones', 'Tablet', 'Watch'],
    'rating': [4.5, 4.2, None, 4.0, None]
})

products['rating'] = products['rating'].fillna(products['rating'].mean())

print(products)



# Task 4: Replace Missing Duration with Median

songs = pd.DataFrame({
    'song': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E'],
    'duration': [210, 185, None, 240, None]
})

songs['duration'] = songs['duration'].fillna(songs['duration'].median())

songs.to_csv('cleaned_songs.csv', index=False)

print(songs)


# Task 5: Replace Missing Followers with Zero

instagram = pd.DataFrame({
    'username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'followers': [1200, None, 3500, None, 5000]
})

instagram['followers'] = instagram['followers'].fillna(0)

print(instagram)