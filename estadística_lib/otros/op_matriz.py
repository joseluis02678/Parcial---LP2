class matriz:
  def __init__(self, mtr):
    # si se ingresa un número, se convierte en matriz 1x1
    if isinstance(mtr, (int, float)):
      self.mtr = [[mtr]]
      self.fmtr = 1  # filas
      self.cmtr = 1  # columnas

    # si se ingresa una lista o tupla, se asume que ya es una matriz
    elif isinstance(mtr, (list, tuple)):
      self.mtr = mtr
      self.fmtr = len(mtr)       # cantidad de filas
      self.cmtr = len(mtr[0])    # cantidad de columnas

    # si no cumple las condiciones anteriores, se lanza un error
    else:
      raise TypeError("No cumple con las condiciones de una matriz")

  def __add__(self, other):
    # verifica que ambas matrices tengan las mismas dimensiones
    if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
      return f'Operacion no valida. Matrices con diferentes dimesiones'
    else:
      nmtr = []   # nueva matriz
      nfmtr = []  # nueva fila temporal
      # suma elemento a elemento
      for i in range(self.fmtr):
        for j in range(self.cmtr):
          nfmtr.append(self.mtr[i][j] + other.mtr[i][j])
        nmtr.append(nfmtr)
        nfmtr = []  # reinicia la fila
      return matriz(nmtr)

  def __sub__(self, other):
    # verifica que ambas matrices tengan las mismas dimensiones
    if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
      return f'Operacion no valida. Matrices con diferentes dimesiones'
    else:
      nmtr = []
      nfmtr = []
      # resta elemento a elemento
      for i in range(self.fmtr):
        for j in range(self.cmtr):
          nfmtr.append(self.mtr[i][j] - other.mtr[i][j])
        nmtr.append(nfmtr)
        nfmtr = []
      return matriz(nmtr)

  def __mul__(self, other):
    # caso 1: multiplicación por un escalar (matriz 1x1)
    if other.fmtr == 1 and other.cmtr == 1:
      nmtr = []
      nfmtr = []
      for i in range(self.fmtr):
        for j in range(self.cmtr):
          nfmtr.append(self.mtr[i][j] * other.mtr[0][0])
        nmtr.append(nfmtr)
        nfmtr = []
      return matriz(nmtr)

    # caso 2: multiplicación entre matrices (producto matricial)
    elif self.cmtr == other.fmtr:
      nmtr = []
      for i in range(self.fmtr):
        nfmtr = []
        for j in range(other.cmtr):
          c = 0  # acumulador del producto
          for k in range(other.fmtr):
            c += self.mtr[i][k] * other.mtr[k][j]
          nfmtr.append(c)
        nmtr.append(nfmtr)
      return matriz(nmtr)

    # caso 3: dimensiones no compatibles
    else:
      return f'Operacion no valida. Matrices no cumplen condiciones'

  def deter(self):

    if self.fmtr == 1 and self.cmtr == 1:
      return self.mtr[0][0]

    det = 0
    pri = 0
    mayorc = 0

    # encontrar fila con más ceros
    for i in range(self.fmtr):
        c = 0
        for j in range(self.cmtr):
            if self.mtr[i][j] == 0:
                c += 1
        if c > mayorc:
            mayorc = c
            pri = i

    # expansión por la fila 'pri'
    for i in range(self.cmtr):
        elem = self.mtr[pri][i]
        if elem != 0:
            nm = []
            for k in range(self.fmtr):
              if k != pri:
                fm = []
                for h in range(self.cmtr):
                  if h != i:
                    fm.append(self.mtr[k][h])
                nm.append(fm)

            sub = matriz(nm)
            det += ((-1) ** (pri + i)) * elem * sub.deter()

    return det

  def __repr__(self):
    # muestra la matriz en formato legible al imprimirla
    return '\n'.join(str(fila) for fila in self.mtr)
