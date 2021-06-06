import math
import numpy as np

S0 =100     # Valor inicial del stock
K = 105     # precio strike
T = 1.0     # plazo
r = 0.05    # tasa libre de riesgo
sigma = 0.2 # Volatilidad

I = 100000  # número de simulaciones
np.random.seed(1000)  # semilla aleatoria
z = np.random.standard_normal(I)  # variables aleatorias normales estándar
ST = S0 * np.exp((r - sigma**2/2) * T + sigma * math.sqrt(T)*z)  # Browniano geométrico
hT = np.maximum(ST-K, 0)                                         # función a evaluar
C0 = math.exp(-r*T)*np.mean(hT)                                  # Valuación de la opción
print('Valor de la opción call europea: {:5.4f}.'.format(C0))    # imprime resultado