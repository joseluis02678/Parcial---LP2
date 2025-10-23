from base import EstadisticaBase
import numpy as np
from scipy.special import gamma  # Para factorial/Gamma necesario en chi, t y F
from scipy import stats
import math

class DistribucionesMuestrales(EstadisticaBase):
    """
    Clase para distribuciones muestrales de variables cuantitativas.
    Incluye distribución de proporciones, medias, chi-cuadrado, t de Student y F de Fisher.
    """

    def distribucion_proporcion(self, p, n, x=None):
        media_p = p
        sigma_p = np.sqrt(p * (1 - p) / n)
        if x is None:
            return {"media": media_p, "desviacion_estandar": sigma_p}
        else:
            coef = 1 / (sigma_p * np.sqrt(2 * np.pi))
            expo = np.exp(-0.5 * ((x - media_p) / sigma_p) ** 2)
            return coef * expo

    def distribucion_media_muestral(self, n, x=None):
        media_p = self.media()
        sigma_p = self.desviacion_estandar() / np.sqrt(n)
        if x is None:
            return {"media": media_p, "desviacion_estandar": sigma_p}
        else:
            coef = 1 / (sigma_p * np.sqrt(2 * np.pi))
            expo = np.exp(-0.5 * ((x - media_p) / sigma_p) ** 2)
            return coef * expo

    def chi_cuadrado(self, x, k):
        if x < 0:
            return 0
        coef = 1 / (2 ** (k / 2) * gamma(k / 2))
        expo = np.exp(-x / 2) * x ** (k / 2 - 1)
        return coef * expo

    def t_student(self, t, df):
        """
        Densidad de la distribución t de Student.
        Args:
            t (float): valor de la variable aleatoria
            df (int): grados de libertad
        Returns:
            float: densidad de probabilidad en t
        """
        coef = gamma((df + 1) / 2) / (np.sqrt(df * np.pi) * gamma(df / 2))
        expo = (1 + t ** 2 / df) ** (-(df + 1) / 2)
        return coef * expo

    def f_fisher(self, x, d1, d2):
        """
        Densidad de la distribución F de Fisher.
        Args:
            x (float): valor de la variable aleatoria (x >= 0)
            d1 (int): grados de libertad numerador
            d2 (int): grados de libertad denominador
        Returns:
            float: densidad de probabilidad en x
        """
        if x < 0:
            return 0
        coef = (gamma((d1 + d2) / 2) /
                (gamma(d1 / 2) * gamma(d2 / 2))) * (d1 / d2) ** (d1 / 2)
        expo = x ** (d1 / 2 - 1) * (1 + (d1 / d2) * x) ** (-(d1 + d2) / 2)
        return coef * expo

from scipy import stats
import math

class IC(DistribucionesMuestrales):
    """
    Clase IC (Intervalos de Confianza)
    Reutiliza los métodos de EstadisticaBase y DistribucionesMuestrales.
    """

    def __init__(self, datos):
        super().__init__(datos)

    def media_t(self, alpha=0.05):
        """
        Intervalo de confianza para la media poblacional (σ desconocida)
        usando la distribución t de Student.

        Fórmula:
        a = media_muestral - t(1-alpha/2; n-1) * s / sqrt(n)
        b = media_muestral + t(1-alpha/2; n-1) * s / sqrt(n)
        """
        n = self.contar_datos()
        if n < 2:
            raise ValueError("Se necesitan al menos 2 observaciones para calcular el IC.")

        media_muestral = self.media()
        s = self.desviacion_estandar()
        t_critico = stats.t.ppf(1 - alpha / 2, df=n - 1)
        error_estandar = s / math.sqrt(n)

        a = media_muestral - t_critico * error_estandar
        b = media_muestral + t_critico * error_estandar

        return {
            "a": a,
            "b": b,
            "media_muestral": media_muestral,
            "t_critico": t_critico,
            "error_estandar": error_estandar,
            "nivel_confianza": 1 - alpha
        }

# -------------------- DOCUMENTACIÓN --------------------
"""
# DistribucionesMuestrales - Documentación

## distribucion_proporcion(p, n, x=None)
- Calcula la distribución muestral de una proporción.
- Devuelve media y desviación estándar si x=None.
- Devuelve densidad de probabilidad aproximada normal si se indica un valor x.

## distribucion_media_muestral(n, x=None)
- Calcula la distribución de la media muestral para muestras de tamaño n.
- Devuelve media y desviación estándar si x=None.
- Devuelve densidad de probabilidad aproximada normal si se indica un valor x.

## chi_cuadrado(x, k)
- Calcula la densidad de probabilidad de la distribución chi-cuadrado.
- `x`: valor de la variable aleatoria (x >= 0)
- `k`: grados de libertad
- Retorna la densidad de probabilidad en el valor x.

## t_student(t, df)
- Calcula la densidad de probabilidad de la distribución t de Student.
- `t`: valor de la variable aleatoria
- `df`: grados de libertad
- Retorna la densidad de probabilidad en el valor t.

## f_fisher(x, d1, d2)
- Calcula la densidad de probabilidad de la distribución F de Fisher.
- `x`: valor de la variable aleatoria (x >= 0)
- `d1`: grados de libertad del numerador
- `d2`: grados de libertad del denominador
- Retorna la densidad de probabilidad en el valor x.
"""

