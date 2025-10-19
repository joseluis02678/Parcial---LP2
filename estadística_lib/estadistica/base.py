import numpy as np

class EstadisticaBase:
    """
    Clase base para operaciones estadísticas fundamentales.
    Reglas del proyecto:
    - No usar el módulo 'statistics' de Python.
    - Se permite 'numpy' solo para operaciones matemáticas básicas (sqrt, arrays, potencias).
    """

    def __init__(self, datos):
        """
        Constructor de la clase.
        Recibe una lista o arreglo de datos numéricos.
        """
        self.datos = np.array(datos)

    def contar_datos(self):
        """Retorna la cantidad de datos."""
        return len(self.datos)

    def suma(self):
        """Calcula la suma total de los datos."""
        total = 0
        for valor in self.datos:
            total += valor
        return total

    def media(self):
        """Calcula la media aritmética sin usar funciones de Python."""
        return self.suma() / self.contar_datos()

    def mediana(self):
        """Calcula la mediana ordenando los datos manualmente."""
        datos_ordenados = sorted(self.datos)
        n = self.contar_datos()
        mitad = n // 2

        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    def moda(self):
        """Calcula la moda sin usar librerías externas."""
        frecuencias = {}
        for valor in self.datos:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        max_freq = max(frecuencias.values())
        modas = [k for k, v in frecuencias.items() if v == max_freq]
        return modas if len(modas) > 1 else modas[0]

    def varianza(self):
        """Calcula la varianza muestral sin usar numpy.mean ni statistics."""
        media = self.media()
        suma_cuadrados = 0
        for valor in self.datos:
            suma_cuadrados += (valor - media) ** 2
        return suma_cuadrados / (self.contar_datos() - 1)

    def desviacion_estandar(self):
        """Calcula la desviación estándar usando sqrt de numpy."""
        return np.sqrt(self.varianza())

    def rango(self):
        """Calcula el rango de los datos."""
        minimo = min(self.datos)
        maximo = max(self.datos)
        return maximo - minimo
        
    def coeficiente_variacion(self):
        media = self.media()
        if media == 0:
            return float('inf')  # evita división por cero
        return (self.desviacion_estandar() / media) * 100


