# test_cualitativos.py
from estadística_lib.estadistica.cualitativos import FrecuenciaCualitativa, ModaCualitativa, ComparadorCualitativo

def test_frecuencia_cualitativa():
    datos = ["A", "B", "A", "C", "B", "A"]
    f = FrecuenciaCualitativa(datos)
    resultado = f.analizar()
    assert resultado["Frecuencia absoluta"]["A"] == 3
    assert round(resultado["Frecuencia relativa (%)"]["A"], 2) == 50.0

def test_moda_cualitativa():
    datos = ["rojo", "rojo", "azul", "verde", "rojo"]
    m = ModaCualitativa(datos)
    resultado = m.analizar()
    assert resultado["Moda"] == ["rojo"]
    assert resultado["Frecuencia"] == 3

def test_comparador_cualitativo():
    datos1 = ["hombre", "mujer", "hombre", "mujer"]
    datos2 = ["sí", "sí", "no", "no"]
    c = ComparadorCualitativo(datos1, datos2)
    tabla = c.analizar()
    assert "hombre" in tabla.index
    assert "sí" in tabla.columns

