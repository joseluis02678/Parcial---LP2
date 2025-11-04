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

    def media_z(self, sigma_poblacional, alpha=0.05):
            """
            Intervalo de confianza para la media poblacional (σ conocida)
            usando la distribución Z (Normal).
    
            Fórmula:
            a = media_muestral - Z(1-alpha/2) * σ / sqrt(n)
            b = media_muestral + Z(1-alpha/2) * σ / sqrt(n)
            """
            n = self.contar_datos()
            if n < 1:
                raise ValueError("Se necesita al menos 1 observación.")
    
            media_muestral = self.media()
            z_critico = stats.norm.ppf(1 - alpha / 2)
            error_estandar = sigma_poblacional / math.sqrt(n)
    
            a = media_muestral - z_critico * error_estandar
            b = media_muestral + z_critico * error_estandar
    
            return {
                "a": a,
                "b": b,
                "media_muestral": media_muestral,
                "z_critico": z_critico,
                "error_estandar": error_estandar,
                "nivel_confianza": 1 - alpha
            }
    
    def proporcion(self, alpha=0.05):
            """
            Intervalo de confianza para la proporción poblacional (usando Z).
            Asume que los datos son binarios (0 o 1).
    
            Fórmula (Intervalo de Wald):
            p_gorro = media de los datos (conteo de 1s / n)
            a = p_gorro - Z(1-alpha/2) * sqrt(p_gorro * (1-p_gorro) / n)
            b = p_gorro + Z(1-alpha/2) * sqrt(p_gorro * (1-p_gorro) / n)
            """
            n = self.contar_datos()
            if n < 1:
                raise ValueError("Se necesita al menos 1 observación.")
    
            # Asumimos que la media de datos binarios (0 y 1) es la proporción
            p_gorro = self.media()
    
            # Verificación de que los datos son binarios
            if not all(val in [0, 1] for val in self.datos):
                raise ValueError("Los datos deben ser binarios (0 o 1) para el IC de proporción.")
            
            # Condición para la aproximación normal (n*p >= 5 y n*(1-p) >= 5)
            if n * p_gorro < 5 or n * (1 - p_gorro) < 5:
                print(f"Advertencia: Muestra pequeña (n*p={round(n*p_gorro, 2)}, n*(1-p)={round(n*(1-p_gorro), 2)}).")
                print("El intervalo de confianza de Wald puede ser inexacto.")
    
            z_critico = stats.norm.ppf(1 - alpha / 2)
            
            # Manejo de p_gorro = 0 o 1 para evitar error en sqrt
            if p_gorro == 0 or p_gorro == 1:
                 error_estandar = 0
            else:
                error_estandar = math.sqrt((p_gorro * (1 - p_gorro)) / n)
    
            a = p_gorro - z_critico * error_estandar
            b = p_gorro + z_critico * error_estandar
            
            # Las proporciones no pueden ser < 0 o > 1
            a = max(0, a)
            b = min(1, b)
    
            return {
                "a": a,
                "b": b,
                "p_gorro": p_gorro,
                "z_critico": z_critico,
                "error_estandar": error_estandar,
                "n": n,
                "nivel_confianza": 1 - alpha
            }
    
        def varianza_chi2(self, alpha=0.05):
            """
            Intervalo de confianza para la varianza poblacional (σ^2)
            usando la distribución Chi-Cuadrado.
    
            Fórmula:
            a = (n-1) * s^2 / Chi2(1-alpha/2; n-1)
            b = (n-1) * s^2 / Chi2(alpha/2; n-1)
            """
            n = self.contar_datos()
            if n < 2:
                raise ValueError("Se necesitan al menos 2 observaciones para calcular el IC.")
    
            s_cuadrado = self.varianza()
            gl = n - 1
            
            # Valor crítico superior (deja 1-alpha/2 a la izquierda)
            chi2_critico_sup = stats.chi2.ppf(1 - alpha / 2, df=gl)
            # Valor crítico inferior (deja alpha/2 a la izquierda)
            chi2_critico_inf = stats.chi2.ppf(alpha / 2, df=gl)
            
            numerador = gl * s_cuadrado
    
            # El IC se invierte: el valor crítico grande (sup) va en el límite inferior (a)
            a = numerador / chi2_critico_sup
            # El valor crítico pequeño (inf) va en el límite superior (b)
            b = numerador / chi2_critico_inf
    
            return {
                "a": a,
                "b": b,
                "s_cuadrado_muestral": s_cuadrado,
                "grados_libertad": gl,
                "chi2_inf_critico": chi2_critico_inf,
                "chi2_sup_critico": chi2_critico_sup,
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

# IC (Intervalos de Confianza) - Documentación

## __init__(datos)
- Constructor de la clase.
- `datos`: Lista o arreglo de datos numéricos.
- Hereda todos los métodos de `DistribucionesMuestrales` (y por ende, de `EstadisticaBase`).

## media_t(alpha=0.05)
- Calcula el intervalo de confianza para la media poblacional cuando la desviación
  estándar poblacional (σ) es desconocida. Usa la distribución t de Student.
- `alpha`: Nivel de significancia (por defecto 0.05 para 95% de confianza).
- Retorna un diccionario con los límites (a, b), la media muestral,
  el valor t-crítico, el error estándar y el nivel de confianza.

## media_z(sigma_poblacional, alpha=0.05)
- Calcula el intervalo de confianza para la media poblacional cuando la desviación
  estándar poblacional (σ) es conocida. Usa la distribución Z (Normal).
- `sigma_poblacional`: El valor conocido de σ (desviación estándar poblacional).
- `alpha`: Nivel de significancia (por defecto 0.05).
- Retorna un diccionario con los límites (a, b), la media muestral,
  el valor z-crítico y el error estándar.

## proporcion(alpha=0.05)
- Calcula el intervalo de confianza para la proporción poblacional (p).
- **Importante**: Asume que los `datos` inicializados en la clase
  son una lista de valores binarios (0 y 1).
- Usa la aproximación Normal (Intervalo de Wald).
- `alpha`: Nivel de significancia (por defecto 0.05).
- Retorna un diccionario con los límites (a, b), la proporción muestral (p_gorro),
  el valor z-crítico, el error estándar y el tamaño de muestra (n).
- Emite una advertencia si la muestra es pequeña (np < 5 o n(1-p) < 5).

## varianza_chi2(alpha=0.05)
- Calcula el intervalo de confianza para la varianza poblacional (σ^2).
- Usa la distribución Chi-Cuadrado (χ²).
- `alpha`: Nivel de significancia (por defecto 0.05).
- Retorna un diccionario con los límites (a, b), la varianza muestral (s_cuadrado),
  los grados de libertad y los valores críticos de Chi-Cuadrado (inferior y superior).
"""

