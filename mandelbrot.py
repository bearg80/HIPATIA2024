# Proyecto HIPATIA 2024: El Universo fractal
# Ejemplo Conjunto de Mandelbrot

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x_vals = np.linspace(xmin, xmax, width)
    y_vals = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))
    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            c = complex(x, y)
            z = 0
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z*z + c
                iteration += 1
            img[i, j] = iteration
    return img

def plot_mandelbrot_set(img):
    plt.imshow(img.T, cmap='hot', extent=[-2, 2, -2, 2])
    plt.colorbar()
    plt.title('Conjunto de Mandelbrot')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.show()

# Parámetros del conjunto de Mandelbrot
xmin, xmax = -2, 2
ymin, ymax = -2, 2
width, height = 800, 800
max_iter = 255

# Generar y visualizar el conjunto de Mandelbrot
mandelbrot_img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
plot_mandelbrot_set(mandelbrot_img)
