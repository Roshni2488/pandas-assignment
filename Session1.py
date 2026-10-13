import pandas as pd

# Task 1: Favorite IPL Teams
fav_cricket_teams = pd.Series(['CSK', 'MI', 'RCB', 'KKR', 'RR'])

print(fav_cricket_teams)

# Task 2: Food Orders

food_orders = pd.DataFrame({
    'Item': ['Pizza', 'Burger', 'Biryani'],
    'Restaurant': ['Dominos', 'McDonalds', 'Behrouz Biryani'],
    'Price': [299, 199, 249]
})

print(food_orders)

# Task 3: Instagram Followers

followers = pd.Series([1200, 54000, 780, 150000, 32000])

highest_index = followers.idxmax()
lowest_index = followers.idxmin()

print("Highest follower count:", followers[highest_index])
print("Lowest follower count:", followers[lowest_index])

# Task 4: Playlist

playlist = pd.DataFrame({
    'Song': ['Kesariya', 'Heeriye', 'Apna Bana Le', 'Tum Kya Mile'],
    'Artist': ['Arijit Singh', 'Jasleen Royal', 'Arijit Singh', 'Arijit Singh'],
    'Duration': [4.28, 3.14, 4.21, 4.37]
})

print(playlist[['Song', 'Duration']])