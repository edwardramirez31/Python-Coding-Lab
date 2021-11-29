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

# ecuaciones nodo 1 (F12, F15, Ax, P)
nodo_1_x = np.array([1, cos(angulo_1), 1, 0])
nodo_1_y = np.array([0, sin(angulo_1), 0, -carga_p])

# ecuaciones nodo 2 (F12, F25, P)
nodo_2_x = np.array([-1, cos(angulo_2), -carga_p])
nodo_2_y = np.array([0, sin(angulo_2), carga_p])

# ecuaciones nodo 2 (F34, F35, P)
nodo_3_x = np.array([1, -cos(angulo_2), -carga_p])
nodo_3_y = np.array([0, sin(angulo_2), carga_p])

# ecuaciones nodo 2 (F34, F45, Bx, P)
nodo_4_x = np.array([1, cos(angulo_1), 1, 0])
nodo_4_y = np.array([0, sin(angulo_1), 0, carga_p])

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

