import pandas as pd

class VariableCualitativa:
    """Clase base para variables cualitativas"""
    def __init__(self, datos):
        self.datos = datos
        self.n = len(datos)
        self.series = pd.Series(datos)
    
    def analizar(self):
        raise NotImplementedError("Este método debe implementarse en las subclases.")
    
    def mostrar(self):
        raise NotImplementedError("Este método debe implementarse en las subclases.")


class FrecuenciaCualitativa(VariableCualitativa):
    """Calcula frecuencias absolutas y relativas"""
    def analizar(self):
        self.frecuencia_abs = self.series.value_counts().to_dict()
        self.frecuencia_rel = (self.series.value_counts(normalize=True) * 100).round(2).to_dict()
        return {
            "Frecuencia absoluta": self.frecuencia_abs,
            "Frecuencia relativa (%)": self.frecuencia_rel
        }
    
    def mostrar(self):
        print("Frecuencias cualitativas:")
        for categoria in self.frecuencia_abs:
            print(f"{categoria}: abs={self.frecuencia_abs[categoria]}, rel={self.frecuencia_rel[categoria]}%")
        print(f"Total de datos: {self.n}")


class ModaCualitativa(VariableCualitativa):
    """Obtiene la moda (categoría más frecuente)"""
    def analizar(self):
        conteo = self.series.value_counts()
        max_freq = conteo.max()
        modas = conteo[conteo == max_freq].index.tolist()
        self.moda = modas
        return {"Moda": modas, "Frecuencia": max_freq}
    
    def mostrar(self):
        print(f"Moda(s): {', '.join(self.moda)}")


class ComparadorCualitativo(VariableCualitativa):
    """Compara dos variables cualitativas (por ejemplo, dos encuestas)"""
    def __init__(self, datos1, datos2):
        super().__init__(datos1)
        self.datos2 = datos2
        self.series2 = pd.Series(datos2)
    
    def analizar(self):
        tabla = pd.crosstab(self.series, self.series2)
        self.tabla = tabla
        return tabla
    
    def mostrar(self):
        print("Tabla de contingencia entre ambas variables:")
        print(self.tabla)