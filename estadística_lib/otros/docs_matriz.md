## **Documentación de la clase `Matriz`**

### **Descripción general**
La clase `Matriz` permite representar y operar con matrices en Python de manera sencilla.  
Está diseñada para trabajar con:

- Matrices de cualquier tamaño (nxm).  
- Escalares (representados como matrices 1x1).  
- Operaciones básicas: suma, resta y multiplicación (escalar o producto matricial).  

Esta implementación **no depende de librerías externas** como `numpy`, por lo que es ideal para entender la lógica de operaciones matriciales desde cero.

---

### **Constructor: `__init__(mtr)`**

Crea una instancia de la clase `Matriz`.

**Parámetros:**

- `mtr` : `int`, `float`, `list` o `tuple`  
  - Si se ingresa un número (`int` o `float`), se convierte en una matriz 1x1.  
  - Si se ingresa una lista o tupla de listas, se interpreta como la matriz completa.  
    - Todas las filas deben tener la misma longitud.  

**Atributos generados:**

- `self.mtr` → lista de listas que representa la matriz.  
- `self.filas` → número de filas.  
- `self.columnas` → número de columnas.  

**Errores posibles:**

- `TypeError` si `mtr` no es un número, lista o tupla.  

**Ejemplos:**

```python
m1 = Matriz(5)                  # matriz 1x1 con valor 5
m2 = Matriz([[1, 2], [3, 4]])   # matriz 2x2

Método: __add__(other)

Suma dos matrices elemento a elemento.

Parámetros:

other : Matriz

Debe tener las mismas dimensiones (filas y columnas) que la matriz original.

Retorna:

Nueva instancia de Matriz con la suma de los elementos.

Si las dimensiones no coinciden, retorna un mensaje de error: "Operación no válida: matrices de diferentes dimensiones".

Ejemplo:

m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
m3 = m1 + m2  # Resultado: [[6, 8], [10, 12]]

Método: __sub__(other)

Resta dos matrices elemento a elemento.

Parámetros:

other : Matriz

Debe tener las mismas dimensiones que la matriz original.

Retorna:

Nueva instancia de Matriz con la resta de los elementos.

Si las dimensiones no coinciden, retorna un mensaje de error: "Operación no válida: matrices de diferentes dimensiones".

Ejemplo:

m1 = Matriz([[5, 6], [7, 8]])
m2 = Matriz([[1, 2], [3, 4]])
m3 = m1 - m2  # Resultado: [[4, 4], [4, 4]]

Método: __mul__(other)

Multiplica la matriz por un escalar o realiza el producto matricial.

Casos:

Multiplicación por escalar (1x1)

other es una matriz 1x1 (other.filas == 1 y other.columnas == 1).

Cada elemento de la matriz original se multiplica por el escalar.

m1 = Matriz([[1, 2], [3, 4]])
scalar = Matriz(2)
m2 = m1 * scalar  # Resultado: [[2, 4], [6, 8]]


Producto matricial

self.columnas debe ser igual a other.filas.

Retorna la matriz resultante del producto matricial clásico.

m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
m3 = m1 * m2  # Resultado: [[19, 22], [43, 50]]


Errores posibles:

Si las dimensiones no son compatibles, retorna: "Operación no válida: dimensiones no compatibles".

Método: __repr__()

Devuelve una representación legible de la matriz para imprimirla en consola.

Ejemplo:

m = Matriz([[1, 2], [3, 4]])
print(m)
# Salida:
# [1, 2]
# [3, 4]

