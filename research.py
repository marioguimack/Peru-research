# ============================================================
# Peru Growth Research Tool
# PART 1 — Data Uploading & Initialization
# Author: Mario
# ============================================================

import pandas as pd
import numpy as np
import glob
import os
# ============================================================
# RESULTS FILE INITIALIZATION & UTILITIES
# ============================================================

import os

# Create results folders
RESULTS_DIR = "results"
PLOTS_DIR = "results/plots"

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

RESULTS_FILE = os.path.join(RESULTS_DIR, "results.md")

# Initialize results.md
with open(RESULTS_FILE, "w") as f:
    f.write("# Peru Growth Research — Results Report\n")
    f.write("Generated automatically by the Peru Research Tool.\n\n")

# Utility to write text blocks into results.md
def write_result(title, content):
    with open(RESULTS_FILE, "a") as f:
        f.write(f"## {title}\n\n")
        f.write("```\n")
        f.write(str(content))
        f.write("\n```\n\n")

# Utility to save plots and reference them in results.md
def save_plot(name):
    path = os.path.join(PLOTS_DIR, f"{name}.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print(f"📁 Saved plot: {path}")

    with open(RESULTS_FILE, "a") as f:
        f.write(f"### Plot: {name}\n")
        f.write(f"![{name}]({path})\n\n")


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
df.to_csv("dataCleaned/dataset_clean.csv", index=False)
# print("✅ Dataset cleaned and saved as data/dataset_clean.csv")

# print(df.info())
# print(df.head())

# ============================================================
# PART 3 — EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("dataCleaned/dataset_clean.csv")

print("\n=== PART 3: EDA STARTED ===")

# ------------------------------------------------------------
# 1. Correlation Matrix
# ------------------------------------------------------------
plt.figure(figsize=(16, 12))
corr = df.corr()
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap — Peru Growth Research")
plt.tight_layout()
plt.show()

save_plot("correlation_heatmap")

# ------------------------------------------------------------
# 2. Time Series Plots for Key Variables
# ------------------------------------------------------------
key_vars = [
    "pbi_real_pct",
    "inversion_privada_pct_pbi",
    "inversion_publica_pct_pbi",
    "formacion_bruta_de_capital_fijo_pct_del_pib",
    "transferencias_corrientes_pct_pbi",
    "gastos_corrientes_pct_pbi"
]

plt.figure(figsize=(14, 8))
for var in key_vars:
    if var in df.columns:
        plt.plot(df["year"], df[var], label=var)

plt.title("Key Economic Variables Over Time")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 8))
for var in key_vars:
    if var in df.columns:
        plt.plot(df["year"], df[var], label=var)

# ------------------------------------------------------------
# 3. Scatterplots — Investment vs GDP Growth
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["inversion_privada_pct_pbi"],
    y=df["pbi_real_pct"]
)
plt.title("Private Investment vs GDP Growth")
plt.xlabel("Private Investment (% PBI)")
plt.ylabel("GDP Real Growth (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["formacion_bruta_de_capital_fijo_pct_del_pib"],
    y=df["pbi_real_pct"]
)
plt.title("Capital Formation vs GDP Growth")
plt.xlabel("FBCF (% PBI)")
plt.ylabel("GDP Real Growth (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

sns.scatterplot(x=df["inversion_privada_pct_pbi"], y=df["pbi_real_pct"])
plt.title("Private Investment vs GDP Growth")
save_plot("scatter_private_investment_vs_growth")
plt.show()

# ------------------------------------------------------------
# 4. Scatterplots — Subsidies vs GDP Growth
# ------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["transferencias_corrientes_pct_pbi"],
    y=df["pbi_real_pct"]
)
plt.title("Current Transfers vs GDP Growth")
plt.xlabel("Transfers (% PBI)")
plt.ylabel("GDP Real Growth (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["gastos_corrientes_pct_pbi"],
    y=df["pbi_real_pct"]
)
plt.title("Current Expenditure vs GDP Growth")
plt.xlabel("Current Expenditure (% PBI)")
plt.ylabel("GDP Real Growth (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 5. Histograms of All Variables
# ------------------------------------------------------------
df.hist(figsize=(18, 14), bins=20)
plt.suptitle("Distribution of All Variables")
plt.tight_layout()
plt.show()


# print("✅ PART 3: EDA Completed Successfully")

# ============================================================
# PART 4 — ECONOMETRIC MODELING
# ============================================================

import pandas as pd
import statsmodels.api as sm
from linearmodels.iv import IV2SLS
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

print("\n=== PART 4: Econometric Modeling Started ===")

# ------------------------------------------------------------
# 1. Load cleaned dataset
# ------------------------------------------------------------
df = pd.read_csv("dataCleaned/dataset_clean.csv")

# ------------------------------------------------------------
# 2. Define dependent and independent variables
# ------------------------------------------------------------
y = df["pbi_real_pct"]  # GDP growth

X = df[[
    "inversion_privada_pct_pbi",
    "inversion_publica_pct_pbi",
    "formacion_bruta_de_capital_fijo_pct_del_pib",
    "transferencias_corrientes_pct_pbi",
    "gastos_corrientes_pct_pbi",
    "deuda_publica_pct_pbi",
    "indice_de_precios_al_consumidor_ipc"
]]

X = sm.add_constant(X)

# ------------------------------------------------------------
# 3. OLS Regression
# ------------------------------------------------------------
ols_model = sm.OLS(y, X).fit()
print("\n=== OLS RESULTS ===")
print(ols_model.summary())

write_result("OLS Regression Results", ols_model.summary().as_text())

# ------------------------------------------------------------
# 4. IV / 2SLS Regression (Investment Private is endogenous)
# ------------------------------------------------------------
# Endogenous regressor
endog = df["inversion_privada_pct_pbi"]

# Instruments
instr = df[[
    "tasa_de_referencia_bcrp",
    "expectativas_empresariales_totales___indice_de_expectativas_de_la_economia_a_12_meses",
    "cotizaciones_internacionales___cobre___lme_us$_por_libras"
]]

# Exogenous regressors
exog = df[[
    "inversion_publica_pct_pbi",
    "formacion_bruta_de_capital_fijo_pct_del_pib",
    "transferencias_corrientes_pct_pbi",
    "gastos_corrientes_pct_pbi",
    "deuda_publica_pct_pbi",
    "indice_de_precios_al_consumidor_ipc"
]]

exog = sm.add_constant(exog)

iv_model = IV2SLS(
    dependent=y,
    exog=exog,
    endog=endog,
    instruments=instr
).fit()

print("\n=== IV / 2SLS RESULTS ===")
print(iv_model.summary)


write_result("IV / 2SLS Results", str(iv_model.summary))


# ------------------------------------------------------------
# 5. Random Forest — Variable Importance
# ------------------------------------------------------------
rf = RandomForestRegressor(n_estimators=500, random_state=42)
rf.fit(X, y)

importance = pd.DataFrame({
    "variable": X.columns,
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=False)

print("\n=== RANDOM FOREST VARIABLE IMPORTANCE ===")
print(importance)

plt.figure(figsize=(10, 6))
sns.barplot(data=importance, x="importance", y="variable")
plt.title("Variable Importance — Random Forest")
plt.tight_layout()
plt.show()


write_result("Random Forest Variable Importance", importance.to_string())

plt.figure(figsize=(10, 6))
sns.barplot(data=importance, x="importance", y="variable")
plt.title("Variable Importance — Random Forest")
save_plot("random_forest_importance")
plt.show()


print("✅ PART 4: Econometric Modeling Completed Successfully")

# ============================================================
# PART 5 — TIME SERIES & FORECASTING
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from statsmodels.tsa.api import VAR

print("\n=== PART 5: Time Series & Forecasting Started ===")

# ------------------------------------------------------------
# 1. Load cleaned dataset
# ------------------------------------------------------------
df = pd.read_csv("dataCleaned/dataset_clean.csv")

# Select key macro variables for time series
ts_vars = [
    "pbi_real_pct",
    "inversion_privada_pct_pbi",
    "inversion_publica_pct_pbi",
    "formacion_bruta_de_capital_fijo_pct_del_pib",
    "gastos_corrientes_pct_pbi"
]

ts_df = df[ts_vars].copy()
ts_df.index = df["year"]

# ------------------------------------------------------------
# 2. ADF Test (Stationarity)
# ------------------------------------------------------------
print("\n=== ADF STATIONARITY TESTS ===")
for col in ts_df.columns:
    result = adfuller(ts_df[col])
    print(f"\nVariable: {col}")
    print(f"ADF Statistic: {result[0]:.4f}")
    print(f"p-value: {result[1]:.4f}")
    if result[1] < 0.05:
        print("→ Stationary (rejects unit root)")
    else:
        print("→ Non-stationary (fails to reject unit root)")

for col in ts_df.columns:
    result = adfuller(ts_df[col])
    write_result(
        f"ADF Test — {col}",
        f"ADF Statistic: {result[0]}\np-value: {result[1]}"
    )


# ------------------------------------------------------------
# 3. Johansen Cointegration Test
# ------------------------------------------------------------
print("\n=== JOHANSEN COINTEGRATION TEST ===")
johansen = coint_johansen(ts_df, det_order=0, k_ar_diff=1)
print("Eigenvalues:", johansen.eig)
print("Trace Statistic:", johansen.lr1)
print("Critical Values (90%, 95%, 99%):")
print(johansen.cvt)

write_result(
    "Johansen Cointegration Test",
    f"Eigenvalues:\n{johansen.eig}\n\n"
    f"Trace Statistic:\n{johansen.lr1}\n\n"
    f"Critical Values:\n{johansen.cvt}"
)


# ------------------------------------------------------------
# 4. VAR Model
# ------------------------------------------------------------
# First difference if needed
ts_df_diff = ts_df.diff().dropna()

model = VAR(ts_df_diff)
results = model.fit(maxlags=2)

print("\n=== VAR MODEL SUMMARY")

write_result("VAR Model Summary", str(results.summary()))
   


# ------------------------------------------------------------
# 5. Forecasting (5 years ahead)
# ------------------------------------------------------------
lag_order = results.k_ar
forecast_input = ts_df_diff.values[-lag_order:]

forecast = results.forecast(y=forecast_input, steps=5)
forecast_df = pd.DataFrame(forecast, columns=ts_df_diff.columns)

print("\n=== 5-YEAR FORECAST (DIFFERENCED SERIES) ===")
print(forecast_df)

write_result("5-Year Forecast (Differenced Series)", forecast_df.to_string())


# ------------------------------------------------------------
# 6. Impulse Response Functions (IRF)
# ------------------------------------------------------------
irf = results.irf(10)

plt.figure(figsize=(12, 8))
irf.plot(orth=True)
plt.suptitle("Impulse Response Functions (IRF)")
plt.tight_layout()
plt.show()

irf.plot(orth=True)
save_plot("irf")
plt.show()


# ------------------------------------------------------------
# 7. Forecast Error Variance Decomposition (FEVD)
# ------------------------------------------------------------
fevd = results.fevd(10)

plt.figure(figsize=(12, 8))
fevd.plot()
plt.suptitle("Forecast Error Variance Decomposition (FEVD)")
plt.tight_layout()
plt.show()

fevd.plot()
save_plot("fevd")
plt.show()


print("✅ PART 5: Time Series & Forecasting Completed Successfully")



