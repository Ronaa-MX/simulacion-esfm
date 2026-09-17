import numpy as np
import matplotlib.pyplot as plt
#Avance
T_total = 20
n_rutas=10
n_pasos = 2000
dt = T_total / n_pasos
t = np.linspace(0, T_total, n_pasos + 1)
dW = np.random.normal(0, np.sqrt(dt), size=(n_rutas, n_pasos))
W = np.cumsum(dW, axis=1)
W = np.hstack([np.zeros((n_rutas,1)), W])
#Rutas con paramétros 10 y 20
plt.figure(figsize=(11,6))
for i in range(n_rutas):
    plt.plot(t, W[i], lw=1.3, alpha=0.85)
    # marcar W_10 y W_20
    plt.scatter([10, 20], [W[i, int(10/dt)], W[i, int(20/dt)]], s=40, zorder=5)
#Rutas de w10 y w20
plt.axvline(10, color='gray', ls='--', alpha=0.6)
plt.axvline(20, color='gray', ls='--', alpha=0.6)
plt.xlabel('Tiempo $t$'); plt.ylabel('$W_t$')
plt.title(f'{n_rutas} trayectorias Brownianas (con $W_{{10}}$ y $W_{{20}}$ marcados)')
plt.grid(True, alpha=0.3)
plt.show()