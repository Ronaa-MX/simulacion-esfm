import numpy as np
import matplotlib.pyplot as plt
from random import gauss, seed
from math import sqrt

def simular_vasicek_euler(x0, m, sigma, c, delta, n):
    """
    Simula una trayectoria del modelo de Vasicek usando Euler-Maruyama.
    Ecuación: dX_t = c * (X_t - m) * dt + sigma * dW_t
    """
    seed(43) # Semilla para reproducibilidad
    oo = sqrt(delta) # Desviación estándar del incremento Browniano
    l = np.zeros(n)
    l[0] = x0
    
    for i in range(n - 1):
        x = l[i]
        t = 0
        # Discretización del intervalo de tiempo [0, 1] en pasos 'delta'
        while t < 1:
            w = oo * gauss(0, 1) # Incremento dW_t ~ N(0, sqrt(delta))
            # Fórmula de Euler-Maruyama
            x = x + c * (x - m) * delta + sigma * w
            t = t + delta
        l[i + 1] = x
        
    return l

# --- Parámetros ---
x0 = 4.3          # Valor inicial
m = 5           # Media de largo plazo
sigma = 0.01    # Volatilidad
c = -0.8        # Velocidad de reversión (negativo para que regrese a m)
delta = 0.001    # Paso de tiempo
n = 100         # Número de datos a generar

# Simulación
trayectoria = simular_vasicek_euler(x0, m, sigma, c, delta, n)

# --- Gráfico ---
plt.figure(figsize=(8, 4))
plt.plot(trayectoria, label='Trayectoria Vasicek', color='blue')
plt.axhline(m, color='red', linestyle='--', label=f'Media m={m}')
plt.title('Modelo de Vasicek (Euler-Maruyama)')
plt.xlabel('Tiempo (pasos)')
plt.ylabel('X_t')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

