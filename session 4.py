import pandas as pd

movies = pd.DataFrame({
    'title': ['Dangal', '3 Idiots', 'PK', 'Shershaah', 'Taare Zameen Par', 'Zindagi Na Milegi Dobara'],
    'rating': [8.3, 8.4, 8.1, 8.4, 8.3, 8.2],
    'release_year': [2016, 2009, 2014, 2021, 2007, 2011]
})

movies_sorted = movies.sort_values(by='rating', ascending=False)

print(movies_sorted)


# Task 2: Sort IPL Teams by Index

ipl = pd.DataFrame({
    'team': ['CSK', 'MI', 'RCB', 'KKR', 'RR'],
    'points': [17, 16, 14, 12, 10],
    'net_run_rate': [0.45, 0.32, 0.18, 0.10, -0.05]
})

ipl = ipl.sort_index(ascending=False)

print(ipl)


# Task 3: Reset YouTube Index

youtube = pd.DataFrame({
    'video_title': ['Python Tutorial', 'Pandas Tutorial', 'SQL Tutorial', 'Power BI Tutorial'],
    'views': [50000, 75000, 90000, 60000],
    'likes': [5000, 7000, 8500, 6500]
}, index=[10, 20, 30, 40])

youtube = youtube.reset_index(drop=True)

print(youtube)


# Task 4: Reindex Zomato Restaurants

zomato = pd.DataFrame({
    'restaurant': ['Dominos', 'McDonalds', 'Zomato Cafe', 'Haldiram'],
    'rating': [4.2, 4.1, 4.5, 4.0]
}, index=['A', 'B', 'C', 'D'])

zomato = zomato.reindex(['C', 'A', 'B', 'D'])

print(zomato)


# Task 5: Sort Flipkart Products by Discount

flipkart = pd.DataFrame({
    'product_name': ['Laptop', 'Mobile', 'Headphones', 'Smart Watch', 'Tablet'],
    'price': [55000, 25000, 2000, 5000, 18000],
    'discount': [10, 25, 40, 30, 15]
})

flipkart = flipkart.sort_values('discount', ascending=False)

flipkart = flipkart.reset_index(drop=True)

print(flipkart)