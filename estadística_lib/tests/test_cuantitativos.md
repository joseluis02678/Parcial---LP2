##  Código de prueba

```python
from base import EstadisticaBase
from cuantitativos import MedidasCuantitativas
import numpy as np

# Datos de niveles de hemoglobina
hemoglobina = [13.2, 14.5, 12.8, 15.1, 11.9, 13.7, 14.2, 
               12.3, 13.9, 15.4, 14.8, 13.1, 12.6, 14.0, 13.4]

hemo = MedidasCuantitativas(hemoglobina)

print("Resumen estadístico:")
for k, v in hemo.resumen_estadistico().items():
    print(f"{k}: {v}")

print("\nCuartiles:", hemo.cuartiles())
print("Percentil 10:", hemo.percentil(10))
print("Percentil 25:", hemo.percentil(25))
print("Percentil 50:", hemo.percentil(50))
print("Percentil 75:", hemo.percentil(75))
print("Percentil 90:", hemo.percentil(90))

![Salida 1](/images/cuantitativos_test.jpg)

