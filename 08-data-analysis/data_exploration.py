
# Data Exploration and Data Quality Checks

from pathlib import Path
import pandas as pd

# Load dataset
data_path = Path(__file__).resolve().parent / "sample_sales.csv"
df = pd.read_csv(data_path)

# Required columns
required_columns = {"Product", "Category", "Quantity", "Unit_Price"}

missing_columns = required_columns - set(df.columns)

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

print("INITIAL DATASET")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

# Create a cleaned copy
df_clean = df.copy()

# Clean text columns
for column in ["Product", "Category"]:
    df_clean[column] = df_clean[column].astype("string").str.strip()
    df_clean[column] = df_clean[column].replace("", pd.NA)

# Convert numeric columns
for column in ["Quantity", "Unit_Price"]:
    df_clean[column] = pd.to_numeric(
        df_clean[column], errors="coerce"
    )

# Data quality checks
print("\nMISSING VALUES")
print(df_clean.isnull().sum())

print("\nDUPLICATE ROWS")
print(df_clean.duplicated().sum())

# Remove duplicates and invalid records
df_clean = df_clean.drop_duplicates()

df_clean = df_clean.dropna(
    subset=["Product", "Category", "Quantity", "Unit_Price"]
)

df_clean = df_clean[
    (df_clean["Quantity"] > 0) &
    (df_clean["Unit_Price"] > 0)
]

print("\nCLEANING SUMMARY")
print("Original rows:", len(df))
print("Cleaned rows:", len(df_clean))
print("Removed rows:", len(df) - len(df_clean))

print("\nCLEANED DATASET")
print(df_clean)

print("\nSTATISTICAL SUMMARY")
print(df_clean.describe())

print("\nDATASET DIMENSIONS")
print(df_clean.shape)
