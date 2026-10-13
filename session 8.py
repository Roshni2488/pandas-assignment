import pandas as pd

# SESSION 8: STRING OPERATIONS IN PANDAS


# TASK 1: Instagram Usernames - Convert to Lowercase
df = pd.DataFrame({
    "username": ["CoolDude", "FoodieQueen", "ROSHNI123", "DataAnalyst", "PythonLearner"]
})

df["username"] = df["username"].str.lower()

print("TASK 1 - Instagram Usernames")
print(df)


# TASK 2: Spotify Song Titles - Remove "Remix"
songs = pd.Series([
    "Perfect Remix",
    "Shape of You",
    "Believer Remix",
    "Faded Remix",
    "Closer"
])

songs = songs.str.replace("Remix", "", regex=False).str.strip()

print("\nTASK 2 - Spotify Songs")
print(songs)


# TASK 3: Zomato Reviews - Find Reviews Mentioning Delivery
df = pd.DataFrame({
    "review": [
        "Fast Delivery",
        "Good food",
        "Late delivery",
        "Excellent service",
        "Delivery was very good"
    ]
})

result = df[df["review"].str.contains("delivery", case=False, na=False)]

print("\nTASK 3 - Zomato Reviews")
print(result)


# TASK 4: Flipkart Categories - Extract Main Category
df = pd.DataFrame({
    "category": [
        "Electronics/Mobiles/Smartphones",
        "Home/Kitchen/Appliances",
        "Fashion/Men/Shirts",
        "Beauty/Makeup/Lipstick"
    ]
})

df["MainCategory"] = df["category"].str.split("/").str[0]

print("\nTASK 4 - Flipkart Categories")
print(df)


# TASK 5: YouTube Titles - Uppercase and Replace Spaces
df = pd.DataFrame({
    "title": [
        "Python tutorial",
        "Pandas for beginners",
        "Data analysis project",
        "Power BI dashboard"
    ]
})

df["title"] = df["title"].str.upper().str.replace(" ", "_", regex=False)

print("\nTASK 5 - YouTube Titles")
print(df)