# Customer Analytics Dashboard (Power BI)

Interactive Power BI dashboard analyzing customer demographics and spending behavior across cities.

![Dashboard](dashboard.png)

## Dataset
Small sample dataset of 15 customers (`customers.csv`) created for practice:

| Column | Description |
|---|---|
| Customer_ID | Unique customer ID |
| Age | Customer age |
| Gender | Female / Male |
| City | Istanbul, Ankara, Izmir, Bursa |
| Annual_Spending | Annual spending amount |

## Dashboard Contents
- **KPI cards:** Total Customers, Total Spending, Avg Spending, Avg Age
- **Total Spending by City:** column chart
- **Age vs Annual Spending:** scatter plot (one point per customer)
- **Avg Spending by Gender:** bar chart
- **Slicers:** City and Gender for interactive filtering

## Key Findings
- 15 customers with a total annual spending of 258,000 (average 17,200) and an average age of about 32.5.
- Istanbul has the highest total spending (about 75,000); Izmir has the lowest (about 55,000).
- Spending rises clearly with age: the youngest customers (early 20s) spend around 9,000-12,000, while customers in their 40s spend 22,000-25,000.
- Average spending is almost the same for male and female customers (about 17,000 each).

## Tools
Power BI Desktop

## Note
This project uses a small sample dataset, so the findings illustrate the analysis approach rather than statistically reliable conclusions.
