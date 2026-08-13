# ============================================================
# Peru Growth Research Tool
# PART 1 — Data Uploading & Initialization
# Author: Mario
# ============================================================

import pandas as pd
import numpy as np
import glob
import os

# ------------------------------------------------------------
# 1. Define data path
# ------------------------------------------------------------
DATA_PATH = "data/"   # your folder with 26 datasets

# ------------------------------------------------------------
# 2. Find all CSV files inside /data
# ------------------------------------------------------------
csv_files = glob.glob(os.path.join(DATA_PATH, "*.csv"))
print(f"📁 Found {len(csv_files)} datasets in /data")

# ------------------------------------------------------------
# 3. Initialize final DataFrame
# ------------------------------------------------------------
df = None

# ------------------------------------------------------------
# 4. Load each CSV, rename its 'value' column, merge by year
# ------------------------------------------------------------
for file in csv_files:
    name = os.path.splitext(os.path.basename(file))[0]

    # Try UTF-8 first, fallback to Latin-1
    try:
        temp = pd.read_csv(file, encoding="utf-8")
    except UnicodeDecodeError:
        temp = pd.read_csv(file, encoding="latin1")

    # --- CLEAN YEAR COLUMN SAFELY ---
    # Convert to string
    temp["year"] = temp["year"].astype(str)

    # Extract only digits (handles weird formats)
    temp["year"] = temp["year"].str.extract(r"(\d+)")

    # Drop rows where year is missing
    temp = temp.dropna(subset=["year"])

    # Convert to integer
    temp["year"] = temp["year"].astype(int)

    # Rename value column
    temp = temp.rename(columns={"value": name})

    # Merge
    if df is None:
        df = temp
    else:
        df = df.merge(temp, on="year", how="outer")

# ------------------------------------------------------------
# 5. Sort by year and convert all columns to numeric
# ------------------------------------------------------------
df = df.sort_values("year")
df = df.apply(pd.to_numeric, errors="coerce")

# ------------------------------------------------------------
# 6. Display structure
# ------------------------------------------------------------
# print("\n=== DATA LOADED SUCCESSFULLY ===")
# print(df.info())
# print(df.head())

# ============================================================
# PART 2 — DATA CLEANING & ECONOMETRIC PREPARATION
# ============================================================

import pandas as pd
import numpy as np
import unicodedata

# ------------------------------------------------------------
# 1. Drop empty columns (e.g., Unnamed: 2)
# ------------------------------------------------------------
df = df.dropna(axis=1, how="all")

# ------------------------------------------------------------
# 2. Normalize column names
# ------------------------------------------------------------
def clean_column(col):
    col = ''.join(
        c for c in unicodedata.normalize('NFD', col)
        if unicodedata.category(c) != 'Mn'
    )
    col = col.lower()
    col = col.replace(" ", "_")
    col = col.replace("%", "pct")
    col = col.replace("(", "").replace(")", "")
    col = col.replace("-", "_")
    col = col.replace(",", "")
    return col

df.columns = [clean_column(c) for c in df.columns]

# ------------------------------------------------------------
# 3. Interpolate missing values
# ------------------------------------------------------------
df = df.interpolate(method="linear")

# ------------------------------------------------------------
# 4. Fill remaining NaNs (pandas 2.0+ syntax)
# ------------------------------------------------------------
df = df.bfill().ffill()

# ------------------------------------------------------------
# 5. Ensure numeric types
# ------------------------------------------------------------
df = df.apply(pd.to_numeric, errors="coerce")

# ------------------------------------------------------------
# 6. Export cleaned dataset
# ------------------------------------------------------------
df.to_csv("data/dataset_clean.csv", index=False)
print("✅ Dataset cleaned and saved as data/dataset_clean.csv")

print(df.info())
print(df.head())
