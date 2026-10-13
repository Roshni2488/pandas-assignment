import pandas as pd

# SESSION 7: COLUMN OPERATIONS & DATA TRANSFORMATIONS


# TASK 1: Flipkart Product Sales - Add TotalValue Column
df = pd.DataFrame({
    "ProductName": ["Phone", "Laptop", "Mouse", "Keyboard"],
    "Price": [20000, 50000, 1000, 1500],
    "Qty": [2, 1, 3, 2]
})

df["TotalValue"] = df["Price"] * df["Qty"]

print("TASK 1 - Flipkart Product Sales")
print(df)


# TASK 2: Food Items - Apply 10% Discount
df = pd.DataFrame({
    "Item": ["Pizza", "Burger", "Pasta", "Sandwich"],
    "Price": [300, 200, 250, 150],
    "Qty": [2, 3, 1, 2]
})

df["DiscountedPrice"] = df["Price"].apply(lambda x: x * 0.90)

print("\nTASK 2 - Food Items")
print(df)


# TASK 3: Instagram Posts - Format Likes and Comments
df = pd.DataFrame({
    "PostID": [1, 2, 3, 4],
    "Likes": [1500, 2000000, 3500000, 800],
    "Comments": [100, 2500, 50000, 75]
})

def format_number(x):
    if x >= 1000000:
        return f"{x/1000000:.1f}M"
    elif x >= 1000:
        return f"{x/1000:.1f}K"
    return str(x)

df["Likes"] = df["Likes"].map(format_number)
df["Comments"] = df["Comments"].map(format_number)

print("\nTASK 3 - Instagram Posts")
print(df)


# TASK 4: Zomato Orders - Calculate FinalAmount
df = pd.DataFrame({
    "Restaurant": ["A", "B", "C", "D"],
    "Price": [200, 300, 150, 400],
    "Qty": [2, 1, 3, 2],
    "DeliveryCharge": [30, 40, 20, 50]
})

df["FinalAmount"] = df.apply(
    lambda row: (row["Price"] * row["Qty"]) + row["DeliveryCharge"],
    axis=1
)

print("\nTASK 4 - Zomato Orders")
print(df)


# TASK 5: Myntra Orders - Calculate GST 5%
df = pd.DataFrame({
    "Product": ["Shirt", "Shoes", "Jeans", "Bag"],
    "Price": [1000, 2000, 1500, 1200],
    "Qty": [2, 1, 2, 1]
})

df["GST"] = (df["Price"] * df["Qty"]) * 0.05

print("\nTASK 5 - Myntra Orders")
print(df)

# Learning:
# 1. apply() and lambda can be used to transform DataFrame values.
# 2. New columns can be created using calculations on existing columns.