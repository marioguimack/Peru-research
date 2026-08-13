# 📘 Peru Growth Research Tool 

## Personal Note

This project was developed independently to advance my skills from university courses in Applied Financial Econometrics, Financial Intermediation, Machine Learning, and Python-based research workflows.  

I used **Microsoft Copilot** as a development companion to structure, debug, and refine the methodology.  
It may still be missing some refinements, but it reflects my progress and learning so far.

## Model Description

The Peru Growth Research Tool is built around a **multi‑method econometric and machine learning pipeline** designed to understand the drivers of Peru’s real GDP growth. Instead of relying on a single model, the tool integrates classical econometrics, machine learning, and time‑series dynamics to produce a robust, policy‑relevant analysis.

### Core Idea

Macroeconomic variables behave differently depending on underlying structural conditions.  
This project identifies and analyzes these conditions using:

- **Static econometric models** (OLS, IV/2SLS)  
- **Predictive machine learning models** (Random Forest)  
- **Dynamic time‑series models** (ADF, Johansen, VAR, IRF, FEVD)

The goal is to extract **stable, interpretable signals** from noisy macroeconomic data and understand how fiscal and investment variables influence growth.

---

## Econometric Framework

### 1. Classical Econometrics (OLS & IV)

These models estimate the direct relationship between growth and its determinants.

- OLS provides baseline coefficients and signs.  
- IV corrects for endogeneity using macroeconomic instruments.  
- **Most variables are statistically insignificant**, reflecting multicollinearity and small sample size.  
- **Current expenditure becomes significant under IV**, confirming its negative impact on growth.

---

### 2. Machine Learning (Random Forest)

Random Forest identifies **which variables matter most**, even when statistical significance is weak.

- Current expenditure is the **dominant negative driver**.  
- Transfers and inflation follow as secondary contributors.  
- Investment variables show lower predictive importance.

---

### 3. Time Series Dynamics (VAR, IRF, FEVD)

These models capture how shocks propagate through the economy.

- Public investment behaves **countercyclically**.  
- Shocks to current expenditure reduce growth **persistently**.  
- FEVD shows growth variance is mostly explained by fiscal variables.

---

## 🧠 Key Findings

Across all econometric methods, the results converge on a robust insight:

> **Current government expenditure is the strongest negative determinant of Peru’s real GDP growth.**

### Additional Findings

Most variables are **statistically insignificant** in OLS and IV, mainly due to:

- multicollinearity  
- small sample size  
- macroeconomic volatility  

Other insights:

- **Private investment** is positively associated with growth but *not statistically significant*.  
- **Public investment** behaves countercyclically but is *not statistically significant*.  
- **FBCF** shows the expected positive sign but is *not statistically significant*.  
- **Inflation** has a mild positive effect but is *not statistically significant*.  
- Growth, investment, and fiscal variables are **cointegrated in the long run**.  
- Shocks to current expenditure have the **largest negative impact** on future growth.

---

## 📊 Econometric Results Summary

### **OLS Regression**

- R² = **0.648**  
- Signs are economically consistent  
- **None of the variables are statistically significant** at conventional levels  
- Multicollinearity is present (**Condition Number ≈ 1500**)

---

### **IV / 2SLS Regression**

- R² = **0.638**  
- **Current expenditure becomes statistically significant (p = 0.017)**  
- All other variables remain **insignificant**, confirming weak statistical power  
- Instruments are economically valid, but sample size limits inference

---

### **Random Forest**

- Provides variable importance ranking  
- Confirms **current expenditure dominates**, even when OLS/IV lack significance  
- Machine learning helps overcome small‑sample limitations by focusing on **predictive relevance**


## Visual Outputs

### 🔥 Correlation Heatmap  
Shows relationships between all macroeconomic variables.  
![Correlation Heatmap](results/plots/correlation_heatmap.png)

---

### 🌲 Random Forest Variable Importance  
Machine learning ranking of which variables matter most for GDP growth.  
![Random Forest Importance](results/plots/random_forest_importance.png)

---

### 📈 Private Investment vs GDP Growth  
Scatterplot showing the relationship between private investment and real GDP growth.  
![Private Investment vs GDP Growth](results/plots/scatter_private_investment_vs_growth.png)

---

### 📉 Impulse Response Functions (IRF)  
Dynamic effects of shocks on GDP growth and investment.  
![IRF](results/plots/irf.png)

---

### 📊 Forecast Error Variance Decomposition (FEVD)  
Shows which variables explain future GDP growth variance.  
![FEVD](results/plots/fevd.png)

---


