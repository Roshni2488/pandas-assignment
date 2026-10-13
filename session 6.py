import pandas as pd
from scipy.stats import zscore




# TASK 1: Spotify Songs - Remove Duplicate Songs
df = pd.DataFrame({
    "song": ["A", "B", "A", "C"],
    "artist": ["X", "Y", "X", "Z"],
    "streams": [100, 200, 100, 300]
})

df = df.drop_duplicates("song")
print("TASK 1 - Spotify Songs")
print(df)


# TASK 2: Flipkart Reviews - Identify Duplicate Reviews
df = pd.DataFrame({
    "product_id": [101, 102, 101, 103, 102],
    "user_id": [1, 2, 1, 3, 2],
    "rating": [5, 4, 5, 3, 4]
})

dup = df[df.duplicated(["product_id", "user_id"], keep=False)]
print("\nTASK 2 - Flipkart Reviews")
print(dup)


# TASK 3: Zomato Orders - Detect Outliers Using IQR
df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "order_amount": [200, 250, 300, 350, 400, 450, 500, 2000]
})

Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["order_amount"] < Q1 - 1.5 * IQR) |
    (df["order_amount"] > Q3 + 1.5 * IQR)
]

print("\nTASK 3 - Zomato Orders")
print(outliers)


# TASK 4: IPL Ticket Sales - Detect Outliers Using Z-Score
df = pd.DataFrame({
    "date": ["01-03", "02-03", "03-03", "04-03",
             "05-03", "06-03", "07-03", "08-03"],
    "tickets_sold": [1200, 1300, 1250, 1400, 1350, 1280, 5000, 1320]
})

df["z_score"] = zscore(df["tickets_sold"])

print("\nTASK 4 - IPL Ticket Sales")
print(df[df["z_score"].abs() > 2])


# TASK 5: Paytm Wallet - Z-Score Function
def find_outliers(df):
    df["z_score"] = zscore(df["transaction_amount"])
    return df[df["z_score"].abs() > 2]

df = pd.DataFrame({
    "transaction_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "transaction_amount": [100, 150, 120, 200, 180, 160, 170, 2000]
})

print("\nTASK 5 - Paytm Wallet")
print(find_outliers(df))