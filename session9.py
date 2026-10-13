import pandas as pd

# SESSION 9: DATE-TIME HANDLING


# TASK 1: Convert Date Strings to Datetime
dates = pd.Series([
    "01-01-2026",
    "15-02-2026",
    "20-03-2026",
    "10-04-2026",
    "25-05-2026"
])

dates = pd.to_datetime(dates, format="%d-%m-%Y")

print("TASK 1 - Convert Dates")
print(dates)


# TASK 2: Extract Year, Month and Day
df = pd.DataFrame({
    "release_date": [
        "10-01-2026",
        "15-02-2025",
        "20-03-2024",
        "25-04-2026"
    ]
})

df["release_date"] = pd.to_datetime(
    df["release_date"],
    format="%d-%m-%Y"
)

df["year"] = df["release_date"].dt.year
df["month"] = df["release_date"].dt.month
df["day"] = df["release_date"].dt.day

print("\nTASK 2 - Extract Year, Month and Day")
print(df)


# TASK 3: Generate Next 7 Days
dates = pd.date_range(
    start=pd.Timestamp.today(),
    periods=7
)

print("\nTASK 3 - Next 7 Days")
print(dates)


# TASK 4: Zomato Gold - Calculate Subscription Tenure
df = pd.DataFrame({
    "user_id": [101, 102, 103, 104],
    "start_date": [
        "01-01-2026",
        "15-02-2026",
        "01-06-2026",
        "20-08-2026"
    ]
})

df["start_date"] = pd.to_datetime(
    df["start_date"],
    format="%d-%m-%Y"
)

df["tenure_days"] = (
    pd.Timestamp.today() - df["start_date"]
).dt.days

print("\nTASK 4 - Zomato Gold Subscription Tenure")
print(df)