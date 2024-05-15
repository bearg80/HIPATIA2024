# Programa HIPATIA 2024: El Universo Fractal
# Conjuntos de Julia
import numpy as np
import matplotlib.pyplot as plt

def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter):
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            z = complex(x, y)
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z*z + c
                iteration += 1
            img[i, j] = iteration
    return img

def plot_julia_set(img):
    plt.imshow(img, cmap='hot', extent=[-2, 2, -2, 2])
    plt.colorbar()
    plt.title('Fractal de Julia')
    plt.xlabel('Parte real')
    plt.ylabel('Parte imaginaria')
    plt.show()

# Parámetros del conjunto de Julia
xmin, xmax = -2, 2
ymin, ymax = -2, 2
width, height = 800, 800
c = complex(-0.7, 0.27015)  # Cambia este valor para explorar diferentes conjuntos de Julia
max_iter = 255

# Generar y visualizar el conjunto de Julia
julia_img = julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter)
plot_julia_set(julia_img)
