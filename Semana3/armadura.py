import numpy as np
from math import atan, cos, sin

# kN
carga_p = 10

# longitudes en metros
L = 2
H = 2
angulo_1 = atan(H / (3 * L / 2))
angulo_2 = atan(H / (L / 2))
A_y, B_y = carga_p, carga_p

# ecuaciones de cada nodo están en el archivo ecuaciones.py

# F12, F15, F25, F34, F35, F45, Ax, Bx
ecuaciones = np.array(
    [
        [1, cos(angulo_1), 0, 0, 0, 0, 1, 0],
        [0, sin(angulo_1), 0, 0, 0, 0, 0, 0],
        [-1, 0, cos(angulo_2), 0, 0, 0, 0, 0],
        [0, 0, sin(angulo_2), 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -cos(angulo_2), 0, 0, 0],
        [0, 0, 0, 0, sin(angulo_2), 0, 0, 0],
        [0, 0, 0, 1, 0, cos(angulo_1), 0, -1],
        [0, 0, 0, 0, 0, sin(angulo_1), 0, 0],
    ]
)

b = np.array([0, -carga_p, -carga_p, carga_p, -carga_p, carga_p, 0, -carga_p])

solucion = np.linalg.solve(ecuaciones, b)

print(solucion)

