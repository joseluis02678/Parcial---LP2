```python
from cualitativos import ResumenCualitativo

# Cargar archivo CSV
ruta = "TelcoCustomerChurn.csv"

# Crear instancia y analizar una columna cualitativa (en este caso se utilizó PaymentMethod
analisis = ResumenCualitativo(ruta, columna="PaymentMethod")

# Obtener resumen
tabla, resumen = analisis.resumen()

print(resumen)
display(tabla)

# Probar polimorfismo: otra variable cualitativa (acá se utilizó Contract)
analisis2 = ResumenCualitativo(ruta, columna="Contract")
tabla2, resumen2 = analisis2.resumen()
print(resumen2)
display(tabla2)
```

![Salida 1](/images/cualitativos_test.png)
