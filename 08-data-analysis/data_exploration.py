# Data Exploration with Pandas

import pandas as pd

df = pd.read_csv("sample_sales.csv")

# First rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Dataset dimensions
print("\nDataset Shape:")
print(df.shape)
