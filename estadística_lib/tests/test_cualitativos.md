```python
from cualitativos import ResumenCualitativo

# Cargar archivo CSV
ruta = "TelcoCustomerChurn.csv"

# Crear instancia y analizar una columna cualitativa (en este caso se utilizó PaymentMethod
analisis = ResumenCualitativo(ruta, columna="PaymentMethod")

# Obtener resumen
tabla, resumen = analisis.resumen()

print("\n RESUMEN ESTADÍSTICO CUALITATIVO - PAYMENTMETHOD \n")
print(resumen)
display(tabla)
#NUEVO: Generar gráficas para la primera variable METHOD
#analisis.graficar_barras()             # (se van retirando los "#" debido a que solo puede mostrar una gráfica a la vez"
#analisis.graficar_pastel()            # (se van retirando los "#" debido a que solo puede mostrar una gráfica a la vez"

# Probar polimorfismo: otra variable cualitativa (acá se utilizó Contract)
analisis2 = ResumenCualitativo(ruta, columna="Contract")
tabla2, resumen2 = analisis2.resumen()

print("\n RESUMEN ESTADÍSTICO CUALITATIVO - CONTRACT \n")
print(resumen2)
display(tabla2)
# NUEVO: Generar gráficos para la segunda variable CONTRACT
#analisis2.graficar_barras()           # (se van retirando los "#" debido a que solo puede mostrar una gráfica a la vez"
analisis2.graficar_pastel()           # (se van retirando los "#" debido a que solo puede mostrar una gráfica a la vez"


```

![Salida 1](/images/cualitativos_test.png)
