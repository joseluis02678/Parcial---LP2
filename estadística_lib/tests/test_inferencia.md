## Análisis de Inferencia: Telco Customer Churn

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from inferencia import DistribucionesMuestrales, IC  

# ==========================================================
# 1️- CARGAR DATA
# ==========================================================
df = pd.read_csv("TelcoCustomerChurn.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

variable = "MonthlyCharges"
data = df[variable].dropna().tolist()

dist_telco = DistribucionesMuestrales(data)
ic_telco = IC(data)

# ==========================================================
# 2️- ESTADÍSTICOS BÁSICOS
# ==========================================================
media = dist_telco.media()
desv = dist_telco.desviacion_estandar()
n = dist_telco.contar_datos()

print("Variable:", variable)
print("Cantidad de datos:", n)
print("Media:", round(media, 3))
print("Desviación estándar:", round(desv, 3))
print("Varianza:", round(dist_telco.varianza(), 3))
```
![Salida 1](../../images/Salida%201%20-%20inferencia.jpg)

