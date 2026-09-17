import numpy as np 
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
sim_n=100000
#Proceso Browniano W_10
w10=np.random.normal(0,np.sqrt(10),sim_n)
#Incremento
increment= np.random.normal(0,np.sqrt(10),sim_n)
#Proceso Browniano W_20
w20=w10+increment
#Coeficiente
corr,p_value = pearsonr(w10,w20)
print(f"Número de simulaciones:({sim_n:,} caminos)")
print(f"p-value: {p_value:.6e}")
print(f"Correlación teórica esperada: {np.sqrt(10)/np.sqrt(20):.4f}")
print(f"Correlación de Montecarlo:{corr:.4f} ")

# --- Gráfico ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 1) Scatter con todos los puntos (submuestreado para no saturar)
idx = np.random.choice(sim_n, size=5000, replace=False)
axes[0].scatter(w10[idx], w20[idx], s=5, alpha=0.3, color='steelblue')
axes[0].set_xlabel(r'$W_{10}$')
axes[0].set_ylabel(r'$W_{20}$')
axes[0].set_title(f'Dispersión $W_{{10}}$ vs $W_{{20}}$\nCorrelación = {corr:.4f}')
axes[0].grid(True, alpha=0.3)

# Línea de regresión visual
m, b = np.polyfit(w10[idx], w20[idx], 1)
xs = np.linspace(w10[idx].min(), w10[idx].max(), 100)
axes[0].plot(xs, m*xs + b, color='red', lw=2, label=f'Pendiente = {m:.3f}')
axes[0].legend()

# 2) Histograma 2D (densidad) para ver mejor la correlación
hb = axes[1].hexbin(w10, w20, gridsize=60, cmap='viridis', bins='log')
axes[1].set_xlabel(r'$W_{10}$')
axes[1].set_ylabel(r'$W_{20}$')
axes[1].set_title('Densidad de puntos (hexbin)')
fig.colorbar(hb, ax=axes[1], label='log(frecuencia)')

plt.tight_layout()
plt.show()