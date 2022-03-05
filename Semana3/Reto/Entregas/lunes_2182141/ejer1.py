import numpy as np
import matplotlib as plt
matriz = np.array([
    [2, 6, 1],
    [1, 2, -1],
    [5, 7, -4]
])
solucion = np.array([7, -1, 9])
print(matriz)
print(solucion)
incog = np.linalg.solve(matriz,solucion)
print(incog)
eje_x = np.arange(0,6)
eje_y = np.arange(3,9)
plt.scatter(eje_x,eje_y)
