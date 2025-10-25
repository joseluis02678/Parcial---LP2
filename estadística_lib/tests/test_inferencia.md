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

### ==========================================================
### 3️- DISTRIBUCIÓN DE LA MEDIA MUESTRAL
### ==========================================================

```python
n_muestra = 30  # tamaño de muestra hipotético
res_media = dist_telco.distribucion_media_muestral(n=n_muestra)

x = np.linspace(media - 3*desv, media + 3*desv, 200)
y = dist_telco.distribucion_media_muestral(n=n_muestra, x=x)

plt.figure(figsize=(8,5))
plt.plot(x, y, color='darkblue', lw=2, label=f'N({media:.1f}, {(desv/np.sqrt(n_muestra)):.2f}²)')
plt.title("Distribución de la Media Muestral")
plt.xlabel("x (Media muestral)")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
```

![Salida 2](../../images/Salida%202%20-%20inferencia.jpg)

### ==========================================================
### 4️- DISTRIBUCIÓN DE LA PROPORCIÓN
### ==========================================================

```python
# Tomamos la proporción de clientes con Churn = Yes
p_hat = (df["Churn"] == "Yes").mean()
n_p = len(df)
res_prop = dist_telco.distribucion_proporcion(p=p_hat, n=n_p)

x_p = np.linspace(p_hat - 0.1, p_hat + 0.1, 200)
y_p = dist_telco.distribucion_proporcion(p=p_hat, n=n_p, x=x_p)

plt.figure(figsize=(8,5))
plt.plot(x_p, y_p, color='green', lw=2, label=f'N({p_hat:.3f}, {np.sqrt(p_hat*(1-p_hat)/n_p):.4f}²)')
plt.title("Distribución de la Proporción (Churn)")
plt.xlabel("Proporción muestral")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
```

![Salida 3](../../images/Salida%203%20-%20inferencia.jpg)

### ==========================================================
### 5️- DISTRIBUCIÓN CHI-CUADRADO
### ==========================================================

```python
x_chi = np.linspace(0, 30, 300)
y_chi = [dist_telco.chi_cuadrado(xi, k=8) for xi in x_chi]

plt.figure(figsize=(8,5))
plt.plot(x_chi, y_chi, color='purple', lw=2)
plt.title("Distribución Chi-cuadrado (k=8)")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.grid(True)
plt.show()
```

![Salida 4](../../images/Salida%204%20-%20inferencia.jpg)

### ==========================================================
### 6️- DISTRIBUCIÓN t DE STUDENT
### ==========================================================

```python
x_t = np.linspace(-4, 4, 300)
y_t = [dist_telco.t_student(ti, df=10) for ti in x_t]

plt.figure(figsize=(8,5))
plt.plot(x_t, y_t, color='red', lw=2, label='t(10 gl)')
plt.title("Distribución t de Student (10 gl)")
plt.xlabel("t")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
```

![Salida 5](../../images/Salida%205%20-%20inferencia.jpg)

### ==========================================================
### 7️- DISTRIBUCIÓN F DE FISHER
### ==========================================================

```python
x_f = np.linspace(0, 5, 300)
y_f = [dist_telco.f_fisher(xi, d1=5, d2=10) for xi in x_f]

plt.figure(figsize=(8,5))
plt.plot(x_f, y_f, color='orange', lw=2, label='F(5,10)')
plt.title("Distribución F de Fisher (5,10)")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
```

![Salida 6](../../images/Salida%206%20-%20inferencia.jpg)

### ==========================================================
### 8️- INTERVALOS DE CONFIANZA (usando clase IC)
### ==========================================================

```python
ic_media = ic_telco.media_t(alpha=0.05)
print("\n Intervalo de confianza (t-Student, 95%) para la media:")
print(f"({ic_media['a']:.2f}, {ic_media['b']:.2f})")

# Graficar el intervalo de confianza
plt.figure(figsize=(6,4))
plt.errorbar(
    x=1,
    y=ic_media["media_muestral"],
    yerr=[[ic_media["media_muestral"] - ic_media["a"]], [ic_media["b"] - ic_media["media_muestral"]]],
    fmt='o', color='blue', ecolor='red', capsize=6
)
plt.title(f"IC al 95% para la media de {variable}")
plt.ylabel(variable)
plt.grid(True)
plt.show()
```

![Salida 7](../../images/Salida%207%20-%20Inferencia.jpg)
