# Category-Based Sales Analysis

import pandas as pd

df = pd.read_csv("sample_sales.csv")

# Calculate revenue
df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"]

# Total quantity by category
quantity_by_category = df.groupby("Category")["Quantity"].sum()

# Total revenue by category
revenue_by_category = df.groupby("Category")["Total_Revenue"].sum()

print("Quantity by Category:")
print(quantity_by_category)

print("\nRevenue by Category:")
print(revenue_by_category)

# Identify the category with the highest revenue
best_category = revenue_by_category.idxmax()

print("\nHighest Revenue Category:")
print(best_category)
