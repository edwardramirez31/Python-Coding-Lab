from math import atan, cos, sin

import numpy as np

np.set_printoptions(suppress=True)

vector = np.array([1, 3, 4, 5])
print(vector)
# 2X + 4Y = 10
# -4X + 5Y = -4
matriz = np.array(
    [
        [2, 4],
        [-4, 5],
    ]
)
vector = np.array([10, -4])

solucion = np.linalg.solve(matriz, vector)

matriz_inversa = np.linalg.inv(matriz)
solucion_2 = matriz_inversa.dot(vector)

print(solucion)

print(solucion_2)

# carga en kN
P = 10
# longitud en metros
L = 2
H = 2

# H SEA VARIABLE ENTRE 1 Y 5, PASO DE 1
# Para cual H las fuerzas son minimas, maximas
By, Ay = P, P

angulo_1 = atan(H / (3 * L / 2))
angulo_2 = atan(H / (L / 2))

# [
#   [H, F25, F34],
#   [H2, F25, F34],
# ]

# F12, F15, F25, F34, F35, F45, Ax, Bx

matriz = np.array(
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

vector = np.array([0, -P, -P, P, -P, P, 0, -P])

solucion = np.linalg.solve(matriz, vector)

print(solucion)
# NODO1
# F15 * cos(angulo) + F12 + Ax = 0
# F15 * sen(angulo) = P

# NODO2
# F25 * cos(angulo) - F12 = -P
# F25 * sen(angulo) = -P

# NODO3
# F34 - F35 * cos(angulo) = -P
# F35 * sen(angulo) = P

# NODO4
# F45 * cos(angulo) + F34 - Bx = 0
# F45 * sen(angulo) = -P

