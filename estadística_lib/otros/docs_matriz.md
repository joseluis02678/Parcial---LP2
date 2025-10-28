# **Documentación de la clase `matriz`**

## **Descripción general**
La clase `matriz` permite representar y operar con matrices en Python de manera sencilla.  
Está diseñada para trabajar con:

- Matrices de cualquier tamaño (n×m).  
- Escalares (representados como matrices 1×1).  
- Operaciones básicas: **suma**, **resta**, **multiplicación** (escalar o producto matricial) y **cálculo del determinante**.  

Esta implementación **no depende de librerías externas** como `numpy`, por lo que es ideal para comprender la lógica interna de las operaciones matriciales desde cero.

---

## **Constructor: `__init__(mtr)`**

Crea una instancia de la clase `matriz`.

### **Parámetros:**
- `mtr` : `int`, `float`, `list` o `tuple`  
  - Si se ingresa un número (`int` o `float`), se convierte en una matriz 1×1.  
  - Si se ingresa una lista o tupla de listas, se interpreta como la matriz completa.  
    - Todas las filas deben tener la misma longitud.  

### **Atributos generados:**
- `self.mtr` → lista de listas que representa la matriz.  
- `self.fmtr` → número de filas.  
- `self.cmtr` → número de columnas.  

### **Errores posibles:**
- `TypeError` si `mtr` no es un número, lista o tupla.  

### **Ejemplos:**
```python
m1 = matriz(5)                  # matriz 1x1 con valor 5
m2 = matriz([[1, 2], [3, 4]])   # matriz 2x2
```

---

## Métodos de la clase `matriz`

---

### **Método:** `__add__(other)`

**Descripción:**  
Suma dos matrices elemento a elemento.

**Parámetros:**
- `other` : `matriz`  
  Debe tener las mismas dimensiones (filas y columnas) que la matriz original.

**Retorna:**  
Nueva instancia de `matriz` con la suma de los elementos.

**Errores posibles:**  
Si las dimensiones no coinciden, retorna el mensaje:  
`"Operacion no valida. Matrices con diferentes dimesiones"`.

**Ejemplo:**
```python
m1 = matriz([[1, 2], [3, 4]])
m2 = matriz([[5, 6], [7, 8]])
m3 = m1 + m2  # Resultado: [[6, 8], [10, 12]]
```

---

### **Método:** `__sub__(other)`

**Descripción:**  
Resta dos matrices elemento a elemento.

**Parámetros:**
- `other` : `matriz`  
  Debe tener las mismas dimensiones que la matriz original.

**Retorna:**  
Nueva instancia de `matriz` con la resta de los elementos.

**Errores posibles:**  
Si las dimensiones no coinciden, retorna el mensaje:  
`"Operacion no valida. Matrices con diferentes dimesiones"`.

**Ejemplo:**
```python
m1 = matriz([[5, 6], [7, 8]])
m2 = matriz([[1, 2], [3, 4]])
m3 = m1 - m2  # Resultado: [[4, 4], [4, 4]]
```

---

### **Método:** `__mul__(other)`

**Descripción:**  
Multiplica la matriz por un escalar o realiza el producto matricial.

**Casos posibles:**

#### 1. **Multiplicación por escalar (1×1):**
Si `other` es una matriz `1×1`, cada elemento de la matriz original se multiplica por ese valor.

```python
m1 = matriz([[1, 2], [3, 4]])
scalar = matriz(2)
m2 = m1 * scalar  # Resultado: [[2, 4], [6, 8]]
```

#### **2. Producto matricial clásico:**

Si `self.cmtr == other.fmtr`, se realiza el producto entre matrices.

```python
m1 = matriz([[1, 2], [3, 4]])
m2 = matriz([[5, 6], [7, 8]])
m3 = m1 * m2  # Resultado: [[19, 22], [43, 50]]
```

#### **3. Dimensiones incompatibles:**

Si las dimensiones no cumplen las condiciones anteriores, retorna:  
`"Operacion no valida. Matrices no cumplen condiciones"`.

---

### **Método:** `deter()`

**Descripción:**  
Calcula el determinante de una matriz cuadrada mediante **expansión por la fila con más ceros**, lo que mejora la eficiencia del cálculo.

**Funcionamiento:**
- Si la matriz es `1×1`, el determinante es el único elemento.  
- Si es de mayor tamaño, se aplica **recursivamente la expansión de cofactores**.  
- Automáticamente selecciona la **fila con más ceros** para reducir operaciones.

**Retorna:**  
Valor numérico del determinante.

**Ejemplo:**
```python
m = matriz([[1, 2, 3],
            [0, 4, 5],
            [1, 0, 6]])

det = m.deter()  # Resultado: 22
```

**Errores posibles:**
Si la matriz no es cuadrada, el método podría generar resultados incorrectos (no se valida en esta versión).

---

### **Método:** `__repr__()`

**Descripción:**  
Devuelve una representación legible de la matriz al imprimirla en consola.

**Ejemplo:**
```python
m = matriz([[1, 2], [3, 4]])
print(m)
# Salida:
# [1, 2]
# [3, 4]
```