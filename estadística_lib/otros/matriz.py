class matriz():
	def __init__(self, mtr):
		self.mtr = mtr
		self.fmtr = len(mtr)
		self.cmtr = len(mtr[0])

	def __add__(self, other):
		if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
			return f'Operacion no valida. Matrices con diferentes dimensiones'
		else:
			nmtr = []
			nfmtr = []
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] + other.mtr[i][j])
				nmtr.append(nfmtr)
				nfmtr = []
			return matriz(nmtr)

	def __sub__(self, other):
		if self.fmtr != other.fmtr or self.cmtr != other.cmtr:
			return f'Operacion no valida. Matrices con diferentes dimensiones'
		else:
			nmtr = []
			nfmtr = []
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] - other.mtr[i][j])
				nmtr.append(nfmtr)
				nfmtr = []
			return matriz(nmtr)

	def __mul__(self, other):
		if other.fmtr == 1 and other.cmtr == 1:
			nmtr = []
			nfmtr = []
			for i in range(self.fmtr):
				for j in range(self.cmtr):
					nfmtr.append(self.mtr[i][j] * other.mtr[0][0])
				nmtr.append(nfmtr)
				nfmtr = []
			return matriz(nmtr)
		elif self.cmtr == other.fmtr:
			nfmtr = []
			for i in range(self.fmtr):
				nfmtr = []
				for j in range(other.cmtr):
					c = 0
					for k in range(other.fmtr):
						c += self.mtr[i][k] * other.mtr[k][j]
					nfmtr.append(c)
				nmtr.append(nfmtr)
			return matriz(nmtr)
		else:
			return f'Operacion no valida. Matrices no cumplen condiciones'

	def __repr__(self):
		return '\n'.join(str(fila) for fila in self.mtr)

