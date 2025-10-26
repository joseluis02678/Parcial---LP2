import pandas as pd
import numpy as np
from estadística_lib.estadistica.base import EstadisticaBase

class ResumenCualitativo(EstadisticaBase):
    """
    Clase para el análisis de variables cualitativas.
    Hereda de EstadisticaBase y aplica conceptos de POO.
    """

    def __init__(self, ruta_archivo, columna=None):
        # Herencia: inicializa la parte común (lectura de CSV)
        super().__init__(ruta_archivo)
        self.columna = columna

    def resumen(self):
        """Genera tabla de frecuencias y moda de una variable cualitativa."""
        df = self.data.copy()

        # Si no se indica la columna, busca automáticamente la primera cualitativa
        if self.columna is None:
            columnas_cuali = df.select_dtypes(exclude=np.number).columns
            if len(columnas_cuali) == 0:
                raise ValueError("No se encontraron columnas cualitativas.")
            self.columna = columnas_cuali[0]

        serie = df[self.columna].astype(str)

        # Cálculo manual de frecuencias
        frecuencias_abs = serie.value_counts()
        frecuencias_rel = serie.value_counts(normalize=True).round(3)
        frecuencias_acu = frecuencias_abs.cumsum()

        # Crear tabla
        tabla = pd.DataFrame({
            "Categoría": frecuencias_abs.index,
            "Frecuencia_Absoluta": frecuencias_abs.values,
            "Frecuencia_Relativa": frecuencias_rel.values,
            "Frecuencia_Acumulada": frecuencias_acu.values
        })

        # Calcular moda
        moda = serie.mode()[0]

        # Resumen general
        resumen_texto = (
            f"Resumen de la variable cualitativa '{self.columna}'\n"
            f"- Total de observaciones: {len(serie)}\n"
            f"- Categorías únicas: {serie.nunique()}\n"
            f"- Moda: {moda}\n"
        )

        return tabla, resumen_texto
