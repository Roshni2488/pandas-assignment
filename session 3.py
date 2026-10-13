import pandas as pd

"""#Task 1 - Movie Data Selection using loc
movies = pd.DataFrame({
    "title": ["Dangal", "3 Idiots", "Pathaan", "Jawan", "PK"],
    "genre": ["Drama", "Comedy", "Action", "Action", "Comedy"],
    "rating": [8.3, 8.4, 6.8, 7.0, 8.1],
    "box_office": [2000, 460, 1050, 1150, 854]
})

result = movies.loc[:, ["title", "rating"]]
movies.loc[:, ["title", "rating"]]

print(result)"""


"""# Task 2 - Flipkart Product Data using iloc

flipkart = pd.DataFrame({
    "product_name": [
        "Laptop", "Mobile", "Headphones", "Smart Watch", "Keyboard",
        "Mouse", "Tablet", "Monitor", "Power Bank", "Earphones"
    ],
    "category": [
        "Electronics", "Electronics", "Accessories", "Wearable",
        "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories"
    ],
    "price": [
        55000, 25000, 1500, 3000, 1200,
        700, 18000, 12000, 1800, 900
    ]
})

result = flipkart.iloc[:10, :]

print(result)"""

"""# Task 3 - Zomato Orders Filtering using Boolean Condition

zomato = pd.DataFrame({
    "restaurant": [
        "Dominos", "Burger King", "Haldiram", "Pizza Hut",
        "Swiggy Cafe", "Biryani House"
    ],
    "order_amount": [450, 650, 800, 350, 900, 550],
    "delivery_time": [30, 35, 40, 25, 45, 38]
})

result = zomato[zomato["order_amount"] > 500]

print(result)"""
"""
# Task 4 - Spotify Songs Filtering using query

spotify = pd.DataFrame({
    "song": [
        "Song A", "Song B", "Song C", "Song D",
        "Song E", "Song F"
    ],
    "artist": [
        "Artist 1", "Artist 2", "Artist 3",
        "Artist 4", "Artist 5", "Artist 6"
    ],
    "streams": [
        1500000, 800000, 2000000,
        1200000, 500000, 1800000
    ],
    "duration": [
        170, 160, 200, 175, 150, 165
    ]
})

result = spotify.query("streams > 1000000 and duration < 180")

print(result)"""

# Task 5 - IPL Matches Filtering using Boolean Indexing

ipl = pd.DataFrame({
    "team1": ["CSK", "MI", "RCB", "KKR", "DC", "CSK"],
    "team2": ["MI", "RCB", "CSK", "DC", "KKR", "RCB"],
    "winner": ["CSK", "MI", "RCB", "KKR", "DC", "CSK"],
    "total_runs": [185, 210, 175, 220, 195, 230]
})

result = ipl[(ipl["total_runs"] >= 180) & (ipl["total_runs"] <= 220)]

print(result)