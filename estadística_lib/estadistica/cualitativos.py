import numpy as np
import pandas as pd
from .base import EstadisticaBase

class EstadisticaCualitativa(EstadisticaBase):
    """
    Clase para análisis estadístico de datos cualitativos (categóricos).
    Hereda de EstadisticaBase e implementa métodos específicos.
    """

    def __init__(self, datos):
        """
        Constructor que recibe una lista de categorías.
        Convierte los datos en un array de tipo string.
        """
        super().__init__(datos)
        self.datos = np.array(datos, dtype=str)

    # --- POLIMORFISMO ---
    def moda(self):
        """
        Sobrescribe el método moda() de la clase base para datos cualitativos.
        Devuelve la categoría más frecuente.
        """
        if len(self.datos) == 0:
            return None

        frecuencias = {}
        for valor in self.datos:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1

        max_freq = max(frecuencias.values())
        modas = [k for k, v in frecuencias.items() if v == max_freq]

        return modas if len(modas) > 1 else modas[0]

    def tabla_frecuencias(self):
        """
        Genera una tabla de frecuencias (absoluta, relativa y acumulada).
        Retorna un DataFrame de pandas.
        """
        if len(self.datos) == 0:
            return pd.DataFrame(columns=["Categoría", "Frecuencia", "Frecuencia Relativa", "Frecuencia Acumulada"])

        # Frecuencia absoluta
        categorias, counts = np.unique(self.datos, return_counts=True)

        # Frecuencia relativa
        total = len(self.datos)
        freq_relativa = counts / total

        # Frecuencia acumulada
        freq_acumulada = np.cumsum(freq_relativa)

        tabla = pd.DataFrame({
            "Categoría": categorias,
            "Frecuencia": counts,
            "Frecuencia Relativa": np.round(freq_relativa, 3),
            "Frecuencia Acumulada": np.round(freq_acumulada, 3)
        })

        return tabla

    def resumen(self):
        """
        Devuelve un resumen textual de las frecuencias.
        """
        tabla = self.tabla_frecuencias()
        moda = self.moda()
        return f"Moda: {moda}\n\nTabla de Frecuencias:\n{tabla}"
