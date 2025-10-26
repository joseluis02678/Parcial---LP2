import pandas as pd
import numpy as np
from base import EstadisticaBase  # usa herencia desde base.py

class ResumenCualitativo(EstadisticaBase):
    """
    Clase para analizar variables cualitativas (hereda de EstadisticaBase).
    Aplica herencia y polimorfismo: redefine moda() para datos no numéricos.
    """

    def __init__(self, ruta_archivo, columna=None):
        """
        Inicializa con un archivo CSV.
        Si se indica una columna, trabajará sobre ella.
        """
        # No usamos super().__init__() aún porque los datos no son numéricos
        self.data = pd.read_csv("TelcoCustomerChurn.csv")
        self.columna = columna

        # Si se especifica columna, guardamos sus valores como array
        if columna is not None:
            super().__init__(self.data[columna].astype(str).values)
        else:
            super().__init__([])

    # Polimorfismo: redefinimos moda() para texto/categorías
    def moda(self):
        """
        Redefine la moda para variables cualitativas.
        """
        if self.columna is None:
            raise ValueError("Debe especificar una columna para calcular la moda.")

        valores = self.data[self.columna].astype(str).values
        frecuencias = {}

        for valor in valores:
            frecuencias[valor] = frecuencias.get(valor, 0) + 1

        max_freq = max(frecuencias.values())
        modas = [k for k, v in frecuencias.items() if v == max_freq]

        return modas if len(modas) > 1 else modas[0]

    def tabla_frecuencias(self):
        """
        Genera tabla de frecuencias absolutas, relativas y acumuladas.
        """
        if self.columna is None:
            columnas_cuali = self.data.select_dtypes(exclude=np.number).columns
            if len(columnas_cuali) == 0:
                raise ValueError("No se encontraron columnas cualitativas.")
            self.columna = columnas_cuali[0]

        serie = self.data[self.columna].astype(str)
        abs_ = serie.value_counts()
        rel_ = serie.value_counts(normalize=True).round(3)
        acu_ = abs_.cumsum()

        tabla = pd.DataFrame({
            "Categoría": abs_.index,
            "Frecuencia_Absoluta": abs_.values,
            "Frecuencia_Relativa": rel_.values,
            "Frecuencia_Acumulada": acu_.values
        })
        return tabla

    def resumen(self):
        """
        Devuelve tabla de frecuencias y resumen textual.
        """
        tabla = self.tabla_frecuencias()
        moda = self.moda()

        resumen_texto = (
            f"Resumen de la variable '{self.columna}'\n"
            f"- Total de observaciones: {len(self.data)}\n"
            f"- Categorías únicas: {self.data[self.columna].nunique()}\n"
            f"- Moda: {moda}\n"
        )
        return tabla, resumen_texto