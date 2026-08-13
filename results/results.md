# Peru Growth Research — Results Report
Generated automatically by the Peru Research Tool.

### Plot: correlation_heatmap
![correlation_heatmap](results/plots/correlation_heatmap.png)

### Plot: scatter_private_investment_vs_growth
![scatter_private_investment_vs_growth](results/plots/scatter_private_investment_vs_growth.png)

## OLS Regression Results

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           pbi_real_pct   R-squared:                       0.648
Model:                            OLS   Adj. R-squared:                  0.511
Method:                 Least Squares   F-statistic:                     4.734
Date:                Thu, 13 Aug 2026   Prob (F-statistic):            0.00365
Time:                        12:06:12   Log-Likelihood:                -60.719
No. Observations:                  26   AIC:                             137.4
Df Residuals:                      18   BIC:                             147.5
Df Model:                           7                                         
Covariance Type:            nonrobust                                         
===============================================================================================================
                                                  coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------------------------
const                                           9.4510     19.522      0.484      0.634     -31.563      50.465
inversion_privada_pct_pbi                       0.7454      0.670      1.113      0.280      -0.661       2.152
inversion_publica_pct_pbi                      -2.0997      2.460     -0.854      0.405      -7.268       3.068
formacion_bruta_de_capital_fijo_pct_del_pib     0.6431      1.117      0.576      0.572      -1.704       2.990
transferencias_corrientes_pct_pbi              -2.1140      1.850     -1.143      0.268      -6.001       1.773
gastos_corrientes_pct_pbi                      -1.3980      0.861     -1.624      0.122      -3.206       0.410
deuda_publica_pct_pbi                           0.1047      0.143      0.734      0.472      -0.195       0.405
indice_de_precios_al_consumidor_ipc             0.6277      0.511      1.227      0.236      -0.447       1.702
==============================================================================
Omnibus:                       22.815   Durbin-Watson:                   2.493
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               38.137
Skew:                           1.788   Prob(JB):                     5.23e-09
Kurtosis:                       7.734   Cond. No.                     1.52e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.52e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

## IV / 2SLS Results

```
                          IV-2SLS Estimation Summary                          
==============================================================================
Dep. Variable:           pbi_real_pct   R-squared:                      0.6381
Estimator:                    IV-2SLS   Adj. R-squared:                 0.4974
No. Observations:                  26   F-statistic:                    137.04
Date:                Thu, Aug 13 2026   P-value (F-stat)                0.0000
Time:                        12:06:13   Distribution:                  chi2(7)
Cov. Estimator:                robust                                         
                                                                              
                                              Parameter Estimates                                              
===============================================================================================================
                                             Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
---------------------------------------------------------------------------------------------------------------
const                                           16.613     21.429     0.7753     0.4382     -25.387      58.613
inversion_publica_pct_pbi                      -2.9296     2.2855    -1.2818     0.1999     -7.4091      1.5500
formacion_bruta_de_capital_fijo_pct_del_pib     1.0686     1.1333     0.9429     0.3457     -1.1526      3.2898
transferencias_corrientes_pct_pbi              -1.6464     1.4731    -1.1176     0.2637     -4.5336      1.2408
gastos_corrientes_pct_pbi                      -1.7679     0.7410    -2.3858     0.0170     -3.2203     -0.3156
deuda_publica_pct_pbi                           0.1300     0.1438     0.9036     0.3662     -0.1520      0.4119
indice_de_precios_al_consumidor_ipc             0.4984     0.4131     1.2063     0.2277     -0.3114      1.3081
inversion_privada_pct_pbi                       0.2686     0.4308     0.6235     0.5329     -0.5758      1.1130
===============================================================================================================

Endogenous: inversion_privada_pct_pbi
Instruments: tasa_de_referencia_bcrp, expectativas_empresariales_totales___indice_de_expectativas_de_la_economia_a_12_meses, cotizaciones_internacionales___cobre___lme_us$_por_libras
Robust Covariance (Heteroskedastic)
Debiased: False
```

## Random Forest Variable Importance

```
                                      variable  importance
5                    gastos_corrientes_pct_pbi    0.566452
4            transferencias_corrientes_pct_pbi    0.185451
7          indice_de_precios_al_consumidor_ipc    0.103057
1                    inversion_privada_pct_pbi    0.046744
3  formacion_bruta_de_capital_fijo_pct_del_pib    0.042780
2                    inversion_publica_pct_pbi    0.033606
6                        deuda_publica_pct_pbi    0.021908
0                                        const    0.000000
```

### Plot: random_forest_importance
![random_forest_importance](results/plots/random_forest_importance.png)

## ADF Test — pbi_real_pct

```
ADF Statistic: -5.717566909974512
p-value: 7.062881546410323e-07
```

## ADF Test — inversion_privada_pct_pbi

```
ADF Statistic: -1.5801007287349564
p-value: 0.49358138282994446
```

## ADF Test — inversion_publica_pct_pbi

```
ADF Statistic: -4.0356740389359285
p-value: 0.001234810285784638
```

## ADF Test — formacion_bruta_de_capital_fijo_pct_del_pib

```
ADF Statistic: -1.391783725530189
p-value: 0.586208703620246
```

## ADF Test — gastos_corrientes_pct_pbi

```
ADF Statistic: -2.6277618383557115
p-value: 0.0873941236274502
```

## Johansen Cointegration Test

```
Eigenvalues:
[8.80707232e-01+0.j 7.38890203e-01+0.j 5.38322658e-01+0.j
 1.89543531e-01+0.j 9.37029455e-05+0.j]

Trace Statistic:
[1.06851102e+02 5.58229119e+01 2.35953691e+01 5.04603252e+00
 2.24897606e-03]

Critical Values:
[[65.8202 69.8189 77.8202]
 [44.4929 47.8545 54.6815]
 [27.0669 29.7961 35.4628]
 [13.4294 15.4943 19.9349]
 [ 2.7055  3.8415  6.6349]]
```

## VAR Model Summary

```
  Summary of Regression Results   
==================================
Model:                         VAR
Method:                        OLS
Date:           Thu, 13, Aug, 2026
Time:                     12:06:14
--------------------------------------------------------------------
No. of Equations:         5.00000    BIC:                    1.55369
Nobs:                     23.0000    HQIC:                 -0.478725
Log likelihood:          -94.8193    FPE:                   0.478567
AIC:                     -1.16162    Det(Omega_mle):       0.0677935
--------------------------------------------------------------------
Results for equation pbi_real_pct
=================================================================================================================
                                                    coefficient       std. error           t-stat            prob
-----------------------------------------------------------------------------------------------------------------
const                                                 -0.766910         1.416901           -0.541           0.588
L1.pbi_real_pct                                       -0.123148         0.944544           -0.130           0.896
L1.inversion_privada_pct_pbi                          -2.343093         2.921799           -0.802           0.423
L1.inversion_publica_pct_pbi                           1.866140         3.656500            0.510           0.610
L1.formacion_bruta_de_capital_fijo_pct_del_pib        -0.704517         1.515523           -0.465           0.642
L1.gastos_corrientes_pct_pbi                           2.718125         2.290473            1.187           0.235
L2.pbi_real_pct                                        0.178350         0.515896            0.346           0.730
L2.inversion_privada_pct_pbi                          -1.897336         1.972821           -0.962           0.336
L2.inversion_publica_pct_pbi                          -0.077786         2.862124           -0.027           0.978
L2.formacion_bruta_de_capital_fijo_pct_del_pib         0.065012         1.705106            0.038           0.970
L2.gastos_corrientes_pct_pbi                           1.163920         1.863589            0.625           0.532
=================================================================================================================

Results for equation inversion_privada_pct_pbi
=================================================================================================================
                                                    coefficient       std. error           t-stat            prob
-----------------------------------------------------------------------------------------------------------------
const                                                 -0.329280         0.213090           -1.545           0.122
L1.pbi_real_pct                                       -0.008081         0.142051           -0.057           0.955
L1.inversion_privada_pct_pbi                          -0.467211         0.439413           -1.063           0.288
L1.inversion_publica_pct_pbi                           0.138942         0.549906            0.253           0.801
L1.formacion_bruta_de_capital_fijo_pct_del_pib         0.268836         0.227922            1.180           0.238
L1.gastos_corrientes_pct_pbi                           0.422562         0.344467            1.227           0.220
L2.pbi_real_pct                                       -0.023515         0.077586           -0.303           0.762
L2.inversion_privada_pct_pbi                          -0.390238         0.296695           -1.315           0.188
L2.inversion_publica_pct_pbi                          -0.289815         0.430439           -0.673           0.501
L2.formacion_bruta_de_capital_fijo_pct_del_pib        -0.003703         0.256433           -0.014           0.988
L2.gastos_corrientes_pct_pbi                           0.091041         0.280268            0.325           0.745
=================================================================================================================

Results for equation inversion_publica_pct_pbi
=================================================================================================================
                                                    coefficient       std. error           t-stat            prob
-----------------------------------------------------------------------------------------------------------------
const                                                 -0.057247         0.060350           -0.949           0.343
L1.pbi_real_pct                                        0.044154         0.040231            1.098           0.272
L1.inversion_privada_pct_pbi                          -0.378103         0.124448           -3.038           0.002
L1.inversion_publica_pct_pbi                          -0.203478         0.155741           -1.307           0.191
L1.formacion_bruta_de_capital_fijo_pct_del_pib         0.176672         0.064550            2.737           0.006
L1.gastos_corrientes_pct_pbi                           0.035726         0.097558            0.366           0.714
L2.pbi_real_pct                                        0.017455         0.021973            0.794           0.427
L2.inversion_privada_pct_pbi                          -0.391950         0.084028           -4.665           0.000
L2.inversion_publica_pct_pbi                          -0.582099         0.121906           -4.775           0.000
L2.formacion_bruta_de_capital_fijo_pct_del_pib         0.416639         0.072625            5.737           0.000
L2.gastos_corrientes_pct_pbi                          -0.058893         0.079375           -0.742           0.458
=================================================================================================================

Results for equation formacion_bruta_de_capital_fijo_pct_del_pib
=================================================================================================================
                                                    coefficient       std. error           t-stat            prob
-----------------------------------------------------------------------------------------------------------------
const                                                  0.070540         0.436885            0.161           0.872
L1.pbi_real_pct                                       -0.055992         0.291239           -0.192           0.848
L1.inversion_privada_pct_pbi                          -0.021036         0.900903           -0.023           0.981
L1.inversion_publica_pct_pbi                          -0.773192         1.127440           -0.686           0.493
L1.formacion_bruta_de_capital_fijo_pct_del_pib         0.403527         0.467294            0.864           0.388
L1.gastos_corrientes_pct_pbi                           0.218501         0.706241            0.309           0.757
L2.pbi_real_pct                                       -0.043450         0.159071           -0.273           0.785
L2.inversion_privada_pct_pbi                          -0.607708         0.608297           -0.999           0.318
L2.inversion_publica_pct_pbi                          -0.207820         0.882503           -0.235           0.814
L2.formacion_bruta_de_capital_fijo_pct_del_pib         0.237846         0.525750            0.452           0.651
L2.gastos_corrientes_pct_pbi                          -0.179011         0.574616           -0.312           0.755
=================================================================================================================

Results for equation gastos_corrientes_pct_pbi
=================================================================================================================
                                                    coefficient       std. error           t-stat            prob
-----------------------------------------------------------------------------------------------------------------
const                                                  0.368587         0.384664            0.958           0.338
L1.pbi_real_pct                                       -0.345854         0.256427           -1.349           0.177
L1.inversion_privada_pct_pbi                           1.354358         0.793218            1.707           0.088
L1.inversion_publica_pct_pbi                          -1.120999         0.992677           -1.129           0.259
L1.formacion_bruta_de_capital_fijo_pct_del_pib         0.357127         0.411438            0.868           0.385
L1.gastos_corrientes_pct_pbi                          -0.884215         0.621824           -1.422           0.155
L2.pbi_real_pct                                       -0.223917         0.140057           -1.599           0.110
L2.inversion_privada_pct_pbi                           0.671736         0.535587            1.254           0.210
L2.inversion_publica_pct_pbi                          -0.054903         0.777017           -0.071           0.944
L2.formacion_bruta_de_capital_fijo_pct_del_pib        -0.321069         0.462907           -0.694           0.488
L2.gastos_corrientes_pct_pbi                          -0.350716         0.505932           -0.693           0.488
=================================================================================================================

Correlation matrix of residuals
                                               pbi_real_pct  inversion_privada_pct_pbi  inversion_publica_pct_pbi  formacion_bruta_de_capital_fijo_pct_del_pib  gastos_corrientes_pct_pbi
pbi_real_pct                                       1.000000                   0.760078                   0.428382                                     0.712465                  -0.884328
inversion_privada_pct_pbi                          0.760078                   1.000000                   0.350504                                     0.620567                  -0.606663
inversion_publica_pct_pbi                          0.428382                   0.350504                   1.000000                                     0.604823                  -0.312232
formacion_bruta_de_capital_fijo_pct_del_pib        0.712465                   0.620567                   0.604823                                     1.000000                  -0.382649
gastos_corrientes_pct_pbi                         -0.884328                  -0.606663                  -0.312232                                    -0.382649                   1.000000



```

## 5-Year Forecast (Differenced Series)

```
   pbi_real_pct  inversion_privada_pct_pbi  inversion_publica_pct_pbi  formacion_bruta_de_capital_fijo_pct_del_pib  gastos_corrientes_pct_pbi
0     -3.111610                  -0.967021                  -0.531661                                    -0.289478                   0.841677
1      2.563681                   0.284405                   0.251558                                     0.687281                   0.202030
2      1.067366                   0.504532                   0.489885                                     0.661822                  -0.473969
3     -2.743017                  -0.756250                  -0.139277                                    -0.424316                   0.100698
4      0.341943                  -0.454220                  -0.096077                                    -0.014031                   0.235345
```

### Plot: irf
![irf](results/plots/irf.png)

### Plot: fevd
![fevd](results/plots/fevd.png)

