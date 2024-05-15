#
# Ejemplo de curva de Koch
import numpy as np
import matplotlib.pyplot as plt

def sierpinski_curve(points, depth):
    if depth == 0:
        return points
    else:
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            q = p1 + (p2 - p1) / 3
            r = p1 + 2 * (p2 - p1) / 3
            s = q + (r - q) * np.cos(np.pi / 3) + (r - q) * np.sin(np.pi / 3) * 1j
            new_points.extend([p1, q, s, r])
        new_points.append(points[-1])
        return sierpinski_curve(new_points, depth - 1)

# Puntos iniciales
points = [0, 0]
for i in range(3):
    points.append(points[-1] + np.exp(2j * np.pi / 3))

# Número de iteraciones
depth = 5

# Generar la curva de Sierpinski
curve = sierpinski_curve(points, depth)

# Extraer las coordenadas x e y
x = np.real(curve)
y = np.imag(curve)

# Visualizar la curva de Sierpinski
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue')
plt.title('Curva de Sierpinski')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
