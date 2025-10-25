import pytest
import pandas as pd
from estadística_lib.estadistica.cualitativos import EstadisticaCualitativa

def test_moda_simple():
    datos = ["rojo", "azul", "rojo", "verde"]
    est = EstadisticaCualitativa(datos)
    assert est.moda() == "rojo"

def test_moda_multiple():
    datos = ["rojo", "azul", "rojo", "azul"]
    est = EstadisticaCualitativa(datos)
    assert set(est.moda()) == {"rojo", "azul"}

def test_tabla_frecuencias():
    datos = ["gato", "perro", "gato", "ave", "gato"]
    est = EstadisticaCualitativa(datos)
    tabla = est.tabla_frecuencias()
    assert isinstance(tabla, pd.DataFrame)
    assert "Frecuencia Relativa" in tabla.columns
    assert tabla["Frecuencia"].sum() == 5

-----------

from estadistica_lib.estadistica.cualitativos import ResumenCualitativo

# Ejemplo de datos cualitativos
datos = ["TV", "Internet", "TV", "Radio", "Internet", "TV", "Radio", "Internet"]

# Crear el objeto
resumen = ResumenCualitativo(datos, "Medio preferido")

# Mostrar el resumen
print(resumen.resumen())