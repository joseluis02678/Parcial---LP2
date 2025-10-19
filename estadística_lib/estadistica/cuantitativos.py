from base import EstadisticaBase
import numpy as np

class MedidasCuantitativas(EstadisticaBase):
	'''
	Clase derivada de EstadisticaBase que agrega medidas específicas para
	variables cuantitativas, incluyendo distribuciones normal y normal estándar.
	'''

	def __init__(self, datos):
		'''
		Inicializa los datos y hereda métodos de EstadisticaBase.
		Args:
			datos (list): Lista o arreglo de valores numéricos.
		'''
		super().__init__(datos) # hereda los atributos y metodos del padre

	# --------- MEDIDAS DE POSICIÓN ----------
	def cuartiles(self):
		'''
		Se calcula los cuartiles (Q1, Q2, Q3) de los datos.
		'''
		datos_ordenados = sorted(self.datos)
		n = self.contar_datos()
		mitad = n // 2
		Q2 = self.mediana() # Se reutliza el método de la clase base

		if n % 2 == 0:
			Q1 = np.median(datos_ordenados[:mitad])
			Q3 = np.median(datos_ordenados[mitad:])
		else:
			Q1 = np.median(datos_ordenados[:mitad])
			Q3 = np.median(datos_ordenados[mitad + 1:])

		return {"Q1": Q1, "Q2": Q2, "Q3": Q3}

	def percentil(self, p):
		'''
		Se calcula el percentil p usando interpolacion lineal.
		Args:
			p (float): Percentil deseado (0-100)
		'''
		if not (0 <= p <= 100):
			raise ValueError("El percentil debe estar entre 0 y 100")

		datos_ordenados = sorted(self.datos)
		n = self.contar_datos()
		k = (p / 100) * (n - 1)
		f = int(np.floor(k))
		c = int(np.ceil(k))

		if f == c:
			return datos_ordenados[f]
		else:
			return datos_ordenados[f] + (k - f) * (datos_ordenados[c] - datos_ordenados[f])

	# ----------- DISTRIBUCIONES --------
	def normal(self, x):
		'''
		Se calcula el valor de la función de densidad de la distribucion
		normal para un valor x
		'''
		mu = self.media()
		sigma = self, desviacion_estandar()
		parte1 = 1 / (sigma * math.sqrt(2 * math.pi))
		parte2 = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
		return parte1 * parte2

	def normal_estandar(self, z):
		'''
		Se calcula el valor de la funcion de densidad de la distribución normal
		estándar (media=0, desviacion=1).
		'''
		parte1 = 1 / math.sqrt(2 * math.pi)
		parte2 = math.exp(-0.5 * (z ** 2))
		return parte1 * parte2

	def z_score(self, x):
		'''
		Se calcula el puntaje z de un valor x.
		'''
		mu = self.media()
		sigma= self.desviacion_estandar()
		return (x - mu) / sigma

	# ---------- RESUMEN GENERAL ---------
	def resumen_estadistico(self):
		''' Devuelve un resumen general con las principales medidas. '''
		return {
			"n": self.contar_datos(),
			"Media": round(self.media(), 2),
			"Mediana": round(self.mediana(), 2),
			"Moda": self.moda(),
			"Varianza": round(self.varianza(), 2),
			"Desviacion estandar": round(self.desviacion_estandar(), 2),
			"Rango": round(self.rango(), 2),
			"Coeficiente de variacion (%)": round(self.coeficiente_variacion(), 2),
			}


