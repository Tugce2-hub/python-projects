# CSV Sales Data Analysis

import pandas as pd

# Read CSV file
df = pd.read_csv("sample_sales.csv")

# Display dataset
print("Sales Data:")
print(df)

# Calculate total revenue
df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"]

print("\nTotal Revenue:")
print(df["Total_Revenue"].sum())

# Revenue by product
print("\nRevenue by Product:")
print(df[["Product", "Total_Revenue"]])

# Revenue by category
print("\nRevenue by Category:")
print(df.groupby("Category")["Total_Revenue"].sum())
