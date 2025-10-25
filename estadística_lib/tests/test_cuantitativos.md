```python
import pandas as pd

# Cargar datos
data = pd.read_csv("TelcoCustomerChurn.csv")

# Ver columnas disponibles
print(data.columns)

import pandas as pd
from base import EstadisticaBase  # importar tu clase

# 1. Cargar el dataset
data = pd.read_csv("TelcoCustomerChurn.csv")

# 2. Seleccionar una variable cuantitativa (por ejemplo MonthlyCharges)
variable = data["MonthlyCharges"].dropna()  # eliminar posibles nulos

# 3. Crear el objeto EstadisticaBase
base_telco = EstadisticaBase(variable)

# 4. Calcular estadísticas descriptivas
print("Cantidad de datos:", base_telco.contar_datos())
print("Suma:", base_telco.suma())
print("Media:", base_telco.media())
print("Mediana:", base_telco.mediana())
print("Moda:", base_telco.moda())
print("Varianza:", base_telco.varianza())
print("Desviación estándar:", base_telco.desviacion_estandar())
print("Rango:", base_telco.rango())
print("Coeficiente de variación:", base_telco.coeficiente_variacion(), "%")


---

### Explicación rápida
- `?raw=true` al final del enlace hace que GitHub **muestre directamente la imagen** (no la vista previa del archivo).  
- Así, las imágenes se verán tanto:
  - En el **navegador (GitHub)**  
  - Como si abres el `.md` desde **VS Code, Obsidian o un visor externo**.  

¿Quieres que también te agregue un pequeño título arriba (por ejemplo “Ejercicio Telco Customer Churn”)?


