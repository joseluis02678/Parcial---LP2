class ResumenCualitativo(EstadisticaBase):
    def __init__(self, ruta_archivo, columna=None):
        super().__init__(ruta_archivo)
        self.columna = columna

    def resumen(self):
        df = self.data.copy()

        # Si no se especifica columna, elegir automáticamente una no numérica
        if self.columna is None:
            cualitativas = df.select_dtypes(exclude="number").columns
            if len(cualitativas) == 0:
                raise ValueError("No se encontraron columnas cualitativas en el archivo.")
            self.columna = cualitativas[0]  # toma la primera

        serie = df[self.columna].astype(str)

        frec_abs = serie.value_counts()
        frec_rel = serie.value_counts(normalize=True).round(2)
        frec_acu = frec_abs.cumsum()

        tabla = pd.DataFrame({
            "Categoría": frec_abs.index,
            "Frecuencia_Absoluta": frec_abs.values,
            "Frecuencia_Relativa": frec_rel.values,
            "Frecuencia_Acumulada": frec_acu.values
        })

        resumen = (
            f"Columna analizada: {self.columna}\n"
            f"Total de observaciones: {len(df)}\n"
            f"Categorías distintas: {serie.nunique()}\n"
            f"Moda: {serie.mode()[0]}"
        )
        return tabla, resumen
