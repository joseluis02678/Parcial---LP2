##  Código de prueba

```python
from op_matriz import matriz

# Matrices ejemplos

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = [
    [2, 4],
    [6, 8]
]

D = [
    [1, 3],
    [5, 7]
]

A1 = matriz(A)
B1 = matriz(B)
C1 = matriz(C)
D1 = matriz(D)
Z1 = matriz(Z)

```

```python

# Suma de matrices

A1 + B1

```

![Salida 1](/images/suma_matriz.png)

```python

# Resta de matrices

A1 - B1

```

![Salida 2](/images/resta_matriz.png)

```python

# Multiplicacion entre matrices

C1 * D1

```

![Salida 3](/images/multi_matriz.png)

```python

# Multiplicacion de una matriz por un escalar

A1 * Z1

```

![Salida 4](/images/multi_escalar_matriz.png)

```python

#Determinante de la matriz A1

A1.deter()

```
![Salida 5](/images/deter1.png)

```python

#Determinante de la matriz B1

B1.deter()

```
![Salida 6](/images/deter1.png)

```python

#Determinante de la matriz C1

C1.deter()

```
![Salida 7](/images/deter2.png)

```python

#Determinante de la matriz D1

D1.deter()

```
![Salida 8](/images/deter2.png)

```python

#Determinante de la matriz Z1

Z1.deter()

```
![Salida 9](/images/deter3.png)

```python

#Transpuesta de la matriz A1

A1.transpuesta()

```
![Salida 10](/images/transpuesta_matri.jpg)

---
---

##  Código de prueba de la estadística matricial

```python

from op_matriz import matriz
from base import EstadisticaBase

F = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

F1 = EstadisticaMatriz(F)

```

```python

F1.media_matricial()

```

![Salida 11](/images/media_matricial.jpg)