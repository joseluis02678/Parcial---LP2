class Matriz:
    def __init__(self, mtr):
        # Si se ingresa un número, se convierte en una matriz 1x1
        if isinstance(mtr, (int, float)):
            self.mtr = [[mtr]]
            self.filas = 1
            self.columnas = 1

        # Si se ingresa una lista o tupla, se asume que ya es una matriz
        elif isinstance(mtr, (list, tuple)):
            self.mtr = [list(fila) for fila in mtr]  # asegurarse que cada fila sea lista
            self.filas = len(mtr)
            self.columnas = len(mtr[0])

        else:
            raise TypeError("No cumple con las condiciones de una matriz")

    def __add__(self, other):
        if self.filas != other.filas or self.columnas != other.columnas:
            return "Operación no válida: matrices de diferentes dimensiones"
        nmtr = [
            [self.mtr[i][j] + other.mtr[i][j] for j in range(self.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(nmtr)

    def __sub__(self, other):
        if self.filas != other.filas or self.columnas != other.columnas:
            return "Operación no válida: matrices de diferentes dimensiones"
        nmtr = [
            [self.mtr[i][j] - other.mtr[i][j] for j in range(self.columnas)]
            for i in range(self.filas)
        ]
        return Matriz(nmtr)

    def __mul__(self, other):
        # Multiplicación por un escalar
        if isinstance(other, Matriz) and other.filas == 1 and other.columnas == 1:
            return Matriz([[self.mtr[i][j] * other.mtr[0][0] for j in range(self.columnas)] 
                           for i in range(self.filas)])

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
        return '\n'.join(str(fila) for fila in self.mtr)


