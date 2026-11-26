
# Función para generar los valores aleatorios del tiempo
t_k <- function(lm) {
  u <- runif(1) # Genera un número aleatorio uniforme entre 0 y 1
  return(-(1/lm) * log(u))
}

# Función para generar el proceso de Poisson de conteo fijo
processo_poisson <- function(n, lm) {
  # Verifica que n sea un número entero positivo
  if (n > 0 && n %% 1 == 0) {
    s <- numeric(n) # Vector numérico de tamaño n (inicializado en 0)
    suma <- 0       # Variable para acumular los tiempos
    
    # En R, los índices de los bucles empiezan en 1, no en 0
    for (i in 1:n) { 
      t_i <- t_k(lm)
      s[i] <- suma
      suma <- suma + t_i # Aquí se acumula el tiempo de llegada
    }
    return(s)
  } else {
    print("De un valor natural para el número de pasos")
  }
}

# Parámetros del proceso de Poisson
lm <- 0.4
n <- 10

# Llamada a la función
s <- processo_poisson(n, lm)

# Datos para la gráfica de pasos
tiempos <- c(0, s) # Concatena el 0 inicial con el vector s
conteos <- 0:n     # Secuencia de 0 a n

# Gráfica de pasos
# type = "s" indica que es una gráfica de escalones (steps)
# lwd = 2 es el grosor de la línea, col = "blue" el color
plot(tiempos, conteos, 
     type = "s", 
     col = "blue", 
     lwd = 2,
     main = "Proceso de Poisson (Conteo Fijo)",
     xlab = "Tiempo",
     ylab = "Llegadas")

# Añadir los puntos en las esquinas (equivalente al marker='o' de Python)
points(tiempos, conteos, col = "blue", pch = 16)

# Añadir la cuadrícula (grid)
grid()