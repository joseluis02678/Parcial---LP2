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
        n = self.contar_datos()
        if n == 0:
            return float('nan') 
        return self.suma() / n

    def mediana(self):
        """Calcula la mediana ordenando los datos manualmente."""
        n = self.contar_datos()
        if n == 0:
            return float('nan')
        
        datos_ordenados = sorted(self.datos)
        mitad = n // 2

        # <-- LÓGICA FALTANTE AÑADIDA
        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    def moda(self):
        """Calcula la moda sin usar librerías externas."""
        n = self.contar_datos()
        if n == 0:
            return [] # Una lista vacía es una respuesta adecuada
        
        frecuencias = {}
        for valor in self.datos:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        
        max_freq = max(frecuencias.values())
        
        # <-- LÓGICA FALTANTE AÑADIDA
        modas = [k for k, v in frecuencias.items() if v == max_freq]
        
        # Si todos los valores son únicos, no hay moda
        if len(modas) == n:
             return []
             
        return modas if len(modas) > 1 else modas[0]

    def varianza(self):
        """Calcula la varianza muestral sin usar numpy.mean ni statistics."""
        n = self.contar_datos()
        # La varianza muestral no está definida para n < 2
        if n < 2:
            return float('nan')
            
        media = self.media()
        suma_cuadrados = 0
        for valor in self.datos:
            suma_cuadrados += (valor - media) ** 2
        # Esta línea ahora es segura
        return suma_cuadrados / (n - 1)

    def desviacion_estandar(self):
        """Calcula la desviación estándar usando sqrt de numpy."""
        return np.sqrt(self.varianza())

    def rango(self):
        """Calcula el rango de los datos."""
        # <-- ¡VERIFICACIÓN AÑADIDA!
        if self.contar_datos() == 0:
            return float('nan')
            
        minimo = min(self.datos)
        maximo = max(self.datos)
        return maximo - minimo
        
    def coeficiente_variacion(self):
        """Calcula el Coeficiente de Variación de Pearson."""
        media = self.media()
        desv_est = self.desviacion_estandar()

        # Casos especiales
        if np.isnan(media) or np.isnan(desv_est):
             return float('nan')
        if media == 0:
            # Si la media es 0 y la desviación también es 0, CV es 0.
            # Si la media es 0 pero hay desviación, CV es infinito.
            return 0.0 if desv_est == 0 else float('inf')
            
        return (desv_est / media) * 100


