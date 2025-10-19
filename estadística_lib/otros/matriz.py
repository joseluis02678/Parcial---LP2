class Matriz:
    """
    Clase para representar y operar con matrices.
    
    Atributos:
    ----------
    mtr : list[list[float]]
        Lista de listas que representa los elementos de la matriz.
    filas : int
        Número de filas de la matriz.
    columnas : int
        Número de columnas de la matriz.
    
    Métodos:
    -------
    __add__(other):
        Suma dos matrices del mismo tamaño.
    __sub__(other):
        Resta dos matrices del mismo tamaño.
    __mul__(other):
        Multiplica por un escalar 1x1 o realiza producto matricial.
    __repr__():
        Representación legible de la matriz al imprimirla.
    """
    
    def __init__(self, mtr):
        """
        Inicializa una matriz.

        Parámetros
        ----------
        mtr : int, float, list o tuple
            Puede ser un número (se crea matriz 1x1) o una lista/tupla de listas que representa la matriz.
        
        Lanza
        -----
        TypeError
            Si el argumento no es número ni lista/tupla.
        """
        if isinstance(mtr, (int, float)):
            self.mtr = [[mtr]]
            self.filas = 1
            self.columnas = 1
        elif isinstance(mtr, (list, tuple)):
            self.mtr = [list(fila) for fila in mtr]  # asegurar que cada fila sea lista
            self.filas = len(mtr)
            self.columnas = len(mtr[0])
        else:
            raise TypeError("No cumple con las condiciones de una matriz")

    def __add__(self, other):
        """
        Suma de matrices elemento a elemento.

        Parámetros
        ----------
        other : Matriz
            Otra instancia de Matriz con las mismas dimensiones.

        Retorna
        -------
        Matriz
            Nueva matriz con la suma de elementos.
        
        Retorna mensaje de error si las dimensiones no coinciden.
        """
        if self.filas != other.filas or self.columnas != other.columnas:
            return "Operación no válida: matrices de diferentes dimensiones"
        
        nmtr = [
            [self.mtr[i][j] + other.mtr[i][j] for j in range(self.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(nmtr)

    def __sub__(self, other):
        """
        Resta de matrices elemento a elemento.

        Parámetros
        ----------
        other : Matriz
            Otra instancia de Matriz con las mismas dimensiones.

        Retorna
        -------
        Matriz
            Nueva matriz con la resta de elementos.
        
        Retorna mensaje de error si las dimensiones no coinciden.
        """
        if self.filas != other.filas or self.columnas != other.columnas:
            return "Operación no válida: matrices de diferentes dimensiones"
        
        nmtr = [
            [self.mtr[i][j] - other.mtr[i][j] for j in range(self.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(nmtr)

    def __mul__(self, other):
        """
        Multiplicación escalar o producto matricial.

        Parámetros
        ----------
        other : Matriz
            Escalar (1x1) o matriz compatible para producto matricial.

        Retorna
        -------
        Matriz
            Nueva matriz con el resultado de la multiplicación.
        
        Retorna mensaje de error si las dimensiones no son compatibles.
        """
        # Multiplicación por escalar 1x1
        if isinstance(other, Matriz) and other.filas == 1 and other.columnas == 1:
            nmtr = [
                [self.mtr[i][j] * other.mtr[0][0] for j in range(self.columnas)]
                for i in range(self.filas)
            ]
            return Matriz(nmtr)

        # Producto matricial
        if self.columnas != other.filas:
            return "Operación no válida: dimensiones no compatibles"
        
        nmtr = [
            [sum(self.mtr[i][k] * other.mtr[k][j] for k in range(self.columnas))
             for j in range(other.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(nmtr)

    def __repr__(self):
        """
        Representación legible de la matriz.

        Retorna
        -------
        str
            Cada fila de la matriz en una línea.
        """
        return '\n'.join(str(fila) for fila in self.mtr)


