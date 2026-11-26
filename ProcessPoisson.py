#Librerías a utilizar
import random as rd 
from math import log
import matplotlib.pyplot as plt
import numpy as np
#Función para generar los valores aleatorios del tiempo
def t_k(lm):
    u = rd.random()
    return -(1/lm)*log(u)
#Función para generar el proceso de Poisson de conteo fijo
def processo_poisson(n,lm):
    if n>0 and isinstance(n,int):
        s = np.zeros(n)
        suma=0
        for i in range(n):
            t_i=t_k(lm)
            suma+=t_i
            s[i]=suma
        return s
    else:
        print("De un valor natural para el número de pasos")
#Párametros del proceso de Poisson
lm = 2
n=15
s=processo_poisson(n,lm)
#Gráfica de pasos del procesos de Poisson
tiempos=[0]+list(s)
conteos = list(range(n+1))
print(s)
plt.step(tiempos,conteos,where='post',color='red',marker='o')
plt.title("Proceso de Poisson(Conteo Fijo)")
plt.xlabel("Tiempo")
plt.ylabel("Llegadas")
plt.grid()
plt.show()
