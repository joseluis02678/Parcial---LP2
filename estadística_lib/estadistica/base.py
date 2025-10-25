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

        # --- LÓGICA FALTANTE AÑADIDA ---
        if n % 2 == 0:
            # Si es par, promedio de los dos centrales
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            # Si es impar, el valor central
            return datos_ordenados[mitad]

    def moda(self):
        """Calcula la moda sin usar librerías externas."""
        n = self.contar_datos()
        if n == 0:
            return [] # Lista vacía, no hay moda
        
        frecuencias = {}
        for valor in self.datos:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1
        
        max_freq = max(frecuencias.values())
        
        # --- LÓGICA FALTANTE AÑADIDA ---
        # Si la frecuencia máxima es 1 (y hay más de 1 dato), todos son únicos, no hay moda
        if max_freq == 1 and n > 1:
             return []

        modas = [k for k, v in frecuencias.items() if v == max_freq]
        
        return modas if len(modas) > 1 else modas[0]

    def varianza(self):
        """Calcula la varianza muestral sin usar numpy.mean ni statistics."""
        n = self.contar_datos()
        if n < 2:
            return float('nan')
            
        media = self.media()
        suma_cuadrados = 0
        for valor in self.datos:
            suma_cuadrados += (valor - media) ** 2
        return suma_cuadrados / (n - 1)

    def desviacion_estandar(self):
        """Calcula la desviación estándar usando sqrt de numpy."""
        var = self.varianza()
        # Si la varianza es nan, la raíz también lo es.
        return np.sqrt(var)

    def rango(self):
        """Calcula el rango de los datos."""
        # --- PROTECCIÓN FALTANTE AÑADIDA ---
        n = self.contar_datos()
        if n == 0:
            return float('nan')
            
        minimo = min(self.datos)
        maximo = max(self.datos)
        return maximo - minimo
        
    def coeficiente_variacion(self):
        """Calcula el Coeficiente de Variación de Pearson."""
        media = self.media()
        desv_est = self.desviacion_estandar()

        # --- LÓGICA DE ROBUSTEZ AÑADIDA ---
        # Si la media o desv es 'nan' (por lista vacía o n<2), el CV es 'nan'
        if np.isnan(media) or np.isnan(desv_est):
             return float('nan')
        
        # Si la media es 0
        if media == 0:
            # Si media y desv son 0 (ej: datos=[0,0,0]), CV es 0
            # Si media es 0 pero hay desv (ej: datos=[-1, 0, 1]), CV es infinito
            return 0.0 if desv_est == 0 else float('inf')
            
        return (desv_est / media) * 100

