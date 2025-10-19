class matriz():
	def __init__(self, mtr):
		#si se ingresa un número, se convierte en una matriz 1x1
		if isinstance(mtr, (int, float)):
			self.mtr = [[mtr]]
			self.fmtr = 1 #nro de filas
			self.cmtr = 1 #nro de columnas

		#si se ingresa una lista o tupla, se asume que ya es una matriz
		elif isinstance(mtr, (list, tuple)):
			self.mtr = mtr
			self.fmtr = len(mtr) #nro de filas
			self.cmtr = len(mtr[0]) #nro de columnas

		#si no cumple las condiciones anteriores, se lanza un error
		else:
			raise TyperError("No cumple con las condiciones de una matriz")

	def __add__(self, other):
		# verifica que ambas matrices tengan las mismas dimensiones
		if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
			return f'Operacion no valida. Matrices con diferentes dimensiones'
		else:
			nmtr = [] # nueva matriz
			nfmtr = [] # nueva fila temporal
			# se suma elemento a elemento
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] + other.mtr[i][j])
				nmtr.append(nfmtr)
				nfmtr = [] # reinicia la fila
			return matriz(nmtr)

	def __sub__(self, other):
		# verifica que ambas matrices tengan las mismas dimensiones
		if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
			return f'Operacion no valida. Matrices con diferentes dimensiones'
		else:
			nmtr = []
			nfmtr = []
			# se resta elemento a elemento
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] - other.mtr[i][j])
				nmtr.append(nfmtr)
				nfmtr = []
			return matriz(nmtr)

	def __mul__(self, other):
		# caso 1: multiplicacion por un escalar (matriz 1x1)
		if other.fmtr == 1 and other.cmtr == 1:
			nmtr = []
			nfmtr = []
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] * other.mtr[0][0])
				nmtr.append(nfmtr)
				nfmtr = []
			return matriz(nmtr)

		# caso 2: multiplicacion entre matrices (producto matricial)
		elif self.cmtr == other.fmtr:
			nfmtr = []
			for i in range(self.fmtr):
				nfmtr = []
				for j in range(other.cmtr):
					c = 0 # acumulador del producto
					for k in range(other.fmtr):
						c += self.mtr[i][k] * other.mtr[k][j]
					nfmtr.append(c)
				nmtr.append(nfmtr)
			return matriz(nmtr)

		# caso 3: dimensiones no compatibles
		else:
			return f'Operacion no valida. Matrices no cumplen condiciones'

	def __repr__(self):
		# muestra la matriz en formato legible al imprimirla
		return '\n'.join(str(fila) for fila in self.mtr)

