# Sales Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_sales.csv")

df["Total_Revenue"] = df["Quantity"] * df["Unit_Price"]

revenue_by_category = df.groupby("Category")["Total_Revenue"].sum()

# Create a bar chart
revenue_by_category.plot(
    kind="bar",
    title="Total Revenue by Category",
    xlabel="Category",
    ylabel="Revenue"
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
