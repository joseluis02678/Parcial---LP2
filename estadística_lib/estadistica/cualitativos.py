import numpy as np
import pandas as pd
from estadística_lib.estadistica.base import EstadisticaBase


class AnalisisCualitativo(EstadisticaBase):
    """
    Clase para análisis de variables cualitativas.
    Permite leer datos desde listas o archivos CSV grandes.
    """

    def __init__(self, datos):
        # Si se pasa una ruta CSV, cargar los datos desde el archivo
        if isinstance(datos, str) and datos.endswith(".csv"):
            df = pd.read_csv(datos)
            # Toma la primera columna como variable cualitativa
            datos = df.iloc[:, 0].dropna().tolist()
        super().__init__(datos)

    def frecuencias(self):
        """Genera tabla de frecuencias absoluta, relativa y acumulada."""
        valores, conteos = np.unique(self.datos, return_counts=True)
        total = len(self.datos)

        df = pd.DataFrame({
            "Categoría": valores,
            "Frecuencia_Absoluta": conteos,
            "Frecuencia_Relativa": np.round(conteos / total, 3),
            "Frecuencia_Acumulada": np.cumsum(conteos)
        })
        return df

    def moda(self):
        """Calcula la moda (categoría más frecuente)."""
        df = self.frecuencias()
        max_frec = df["Frecuencia_Absoluta"].max()
        modas = df.loc[df["Frecuencia_Absoluta"] == max_frec, "Categoría"].tolist()
        return modas if len(modas) > 1 else modas[0]


class ResumenCualitativo(AnalisisCualitativo):
    """
    Clase que amplía AnalisisCualitativo para mostrar resumen general.
    Ejemplo de herencia y polimorfismo.
    """

    def __init__(self, datos):
        super().__init__(datos)

    def resumen(self):
        """Devuelve tabla de frecuencias y resumen textual."""
        df = self.frecuencias()
        moda_valor = self.moda()

        resumen_texto = (
            f"Total de observaciones: {self.contar_datos()}\n"
            f"Categorías distintas: {len(df)}\n"
            f"Moda: {moda_valor}"
        )
        return df, resumen_texto


# Ejemplo de uso local (puedes probar esto para verificar)
if __name__ == "__main__":
    # Ejemplo con lista
    datos = ["Rojo", "Azul", "Rojo", "Verde", "Azul", "Rojo", "Amarillo"]
    analisis = ResumenCualitativo(datos)
    tabla, resumen = analisis.resumen()
    print(tabla)
    print("\n" + resumen)

    # Ejemplo con CSV
    # analisis_csv = ResumenCualitativo("datos_cualitativos.csv")
    # tabla_csv, resumen_csv = analisis_csv.resumen()
    # print(tabla_csv)
    # print("\n" + resumen_csv)
