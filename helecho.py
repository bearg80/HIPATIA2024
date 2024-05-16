# 16.May/2024
# Creación de un helecho a partir de las funciones de Barnsley
import numpy as np
import matplotlib.pyplot as plt

def barnsley_fern(n_points):
    # Puntos iniciales
    x = np.zeros(n_points)
    y = np.zeros(n_points)
    x[0] = 0
    y[0] = 0

    # Matriz de probabilidades para las funciones de Barnsley
    probs = [0.01, 0.85, 0.07, 0.07]

    # Aplica las funciones de contracción
    for i in range(1, n_points):
        choice = np.random.choice([0, 1, 2, 3], p=probs)
        if choice == 0:
            x[i] = 0
            y[i] = 0.16 * y[i-1]
        elif choice == 1:
            x[i] = 0.85 * x[i-1] + 0.04 * y[i-1]
            y[i] = -0.04 * x[i-1] + 0.85 * y[i-1] + 1.6
        elif choice == 2:
            x[i] = 0.2 * x[i-1] - 0.26 * y[i-1]
            y[i] = 0.23 * x[i-1] + 0.22 * y[i-1] + 1.6
        elif choice == 3:
            x[i] = -0.15 * x[i-1] + 0.28 * y[i-1]
            y[i] = 0.26 * x[i-1] + 0.24 * y[i-1] + 0.44

    return x, y

# Genera puntos del helecho fractal
n_points = 100000
x, y = barnsley_fern(n_points)

# Visualiza el helecho fractal
plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=0.1, color='green')
plt.title('Helecho fractal generado con el Sistema de Funciones de Barnsley')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
