import pandas as pd

# TASK 1: IPL - Display First 10 Rows
df = pd.DataFrame({
    "player_name": ["A", "B", "C", "D", "E"],
    "runs": [500, 450, 600, 300, 400],
    "matches": [10, 12, 15, 8, 10],
    "average": [50, 37.5, 40, 37.5, 40],
    "strike_rate": [140, 130, 150, 125, 135]
})

print("TASK 1")
print(df.head(10))


# TASK 2: Univariate Analysis - Runs
print("\nTASK 2")
print("Mean:", df["runs"].mean())
print("Median:", df["runs"].median())
print("Mode:", df["runs"].mode()[0])
print("Minimum:", df["runs"].min())
print("Maximum:", df["runs"].max())


# TASK 3: Zomato - Correlation between Rating & Votes
zomato = pd.DataFrame({
    "name": ["A", "B", "C", "D", "E"],
    "rating": [4.5, 4.0, 3.5, 4.2, 3.8],
    "votes": [500, 300, 150, 400, 250],
    "avg_cost": [500, 300, 250, 450, 350]
})

print("\nTASK 3")
print("Correlation:", zomato["rating"].corr(zomato["votes"]))


# TASK 4: Summary Statistics
print("\nTASK 4")
print(df.describe())


# TASK 5: Bivariate Analysis - Runs & Matches
print("\nTASK 5")
print("Correlation between Runs and Matches:",
      df["runs"].corr(df["matches"]))