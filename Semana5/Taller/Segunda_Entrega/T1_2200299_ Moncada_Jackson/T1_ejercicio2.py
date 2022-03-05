from gettext import find
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

#Ejrcicio 1

carga_final = (18 * 0.25) + 20
fuerza_P = np.arange(20, carga_final + 0.25, 0.25)
theta = np.arange(0, 190, 10)
theta_radianes = theta * np.pi / 180
theta_1 = math.atan(1/2) #angulo entre AB y AE
theta_2 = math.atan(2) #angulo entre AE y AD

# Ecuaciones de la estática
# Reacciones
Ax = (-1 * np.sin(theta_radianes) * fuerza_P) + (4 * np.cos(theta_radianes) * fuerza_P)
Ay = -1 * np.cos(theta_radianes) * fuerza_P
Dx = -4 * np.cos(theta_radianes) * fuerza_P

# fuerzas internas
# Orden de incógnitas (AB,AD,AE,BC,BE,CE,DE)
# orden de las reacciones (Ax, Ay, Dx)
# DE - Dx = 0
# AD = 0
# AB + np.cos(theta_1) * AE -Ax = 0
# np.sin(theta_1) * AE + Ay = 0
# AB - BC = 0
# BE = 0
# DE + np.cos(theta_1) * AE - np.sin(theta_2) * CE = 0

matriz = np.array([
        [0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, np.cos(theta_1), 0, 0, 0, 0],
        [0, 0, np.sin(theta_1), 0, 0, 0, 0],
        [1, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, np.cos(theta_1), 0, 0, - np.sin(theta_2), 1],
    ])

vector_1 = np.array([Dx[0], 0, Ax[0], -Ay[0], 0, 0, 0])
vector_2 = np.array([Dx[1], 0, Ax[1], -Ay[1], 0, 0, 0])
vector_3 = np.array([Dx[2], 0, Ax[2], -Ay[2], 0, 0, 0])
vector_4 = np.array([Dx[3], 0, Ax[3], -Ay[3], 0, 0, 0])
vector_5 = np.array([Dx[4], 0, Ax[4], -Ay[4], 0, 0, 0])
vector_6 = np.array([Dx[5], 0, Ax[5], -Ay[5], 0, 0, 0])
vector_7 = np.array([Dx[6], 0, Ax[6], -Ay[6], 0, 0, 0])
vector_8 = np.array([Dx[7], 0, Ax[7], -Ay[7], 0, 0, 0])
vector_9 = np.array([Dx[8], 0, Ax[8], -Ay[8], 0, 0, 0])
vector_10 = np.array([Dx[9], 0, Ax[9], -Ay[9], 0, 0, 0])
vector_11 = np.array([Dx[10], 0, Ax[10], -Ay[10], 0, 0, 0])
vector_12 = np.array([Dx[11], 0, Ax[11], -Ay[11], 0, 0, 0])
vector_13 = np.array([Dx[12], 0, Ax[12], -Ay[12], 0, 0, 0])
vector_14 = np.array([Dx[13], 0, Ax[13], -Ay[13], 0, 0, 0])
vector_15 = np.array([Dx[14], 0, Ax[14], -Ay[14], 0, 0, 0])
vector_16 = np.array([Dx[15], 0, Ax[15], -Ay[15], 0, 0, 0])
vector_17 = np.array([Dx[16], 0, Ax[16], -Ay[16], 0, 0, 0])
vector_18 = np.array([Dx[17], 0, Ax[17], -Ay[17], 0, 0, 0])

solucion_1 = np.linalg.solve(matriz, vector_1)
print("Para theta = " + str(theta[0]))
print("reacciones:")
print(Ax[0], Ay[0], Dx[0])
print("F internas: ")
print(solucion_1)

solucion_2 = np.linalg.solve(matriz, vector_2)
print("Para theta = " + str(theta[1]))
print("reacciones:")
print(Ax[1], Ay[1], Dx[1])
print("F internas: ")
print(solucion_2)

solucion_3 = np.linalg.solve(matriz, vector_3)
print("Para theta = " + str(theta[2]))
print("reacciones:")
print(Ax[2], Ay[2], Dx[2])
print("F internas: ")
print(solucion_3)

solucion_4 = np.linalg.solve(matriz, vector_4)
print("Para theta = " + str(theta[3]))
print("reacciones:")
print(Ax[3], Ay[3], Dx[3])
print("F internas: ")
print(solucion_4)

solucion_5 = np.linalg.solve(matriz, vector_5)
print("Para theta = " + str(theta[4]))
print("reacciones:")
print(Ax[4], Ay[4], Dx[4])
print("F internas: ")
print(solucion_4)

solucion_6 = np.linalg.solve(matriz, vector_6)
print("Para theta = " + str(theta[5]))
print("reacciones:")
print(Ax[5], Ay[5], Dx[5])
print("F internas: ")
print(solucion_5)

solucion_7 = np.linalg.solve(matriz, vector_7)
print("Para theta = " + str(theta[6]))
print("reacciones:")
print(Ax[6], Ay[6], Dx[6])
print("F internas: ")
print(solucion_7)

solucion_8 = np.linalg.solve(matriz, vector_8)
print("Para theta = " + str(theta[7]))
print("reacciones:")
print(Ax[7], Ay[7], Dx[7])
print("F internas: ")
print(solucion_8)

solucion_9 = np.linalg.solve(matriz, vector_9)
print("Para theta = " + str(theta[8]))
print("reacciones:")
print(Ax[8], Ay[8], Dx[8])
print("F internas: ")
print(solucion_9)

solucion_10 = np.linalg.solve(matriz, vector_10)
print("Para theta = " + str(theta[9]))
print("reacciones:")
print(Ax[9], Ay[9], Dx[9])
print("F internas: ")
print(solucion_10)

solucion_11 = np.linalg.solve(matriz, vector_11)
print("Para theta = " + str(theta[10]))
print("reacciones:")
print(Ax[10], Ay[10], Dx[10])
print("F internas: ")
print(solucion_11)

solucion_12 = np.linalg.solve(matriz, vector_12)
print("Para theta = " + str(theta[11]))
print("reacciones:")
print(Ax[11], Ay[11], Dx[11])
print("F internas: ")
print(solucion_12)

solucion_13 = np.linalg.solve(matriz, vector_13)
print("Para theta = " + str(theta[12]))
print("reacciones:")
print(Ax[12], Ay[12], Dx[12])
print("F internas: ")
print(solucion_13)

solucion_14 = np.linalg.solve(matriz, vector_14)
print("Para theta = " + str(theta[13]))
print("reacciones:")
print(Ax[13], Ay[13], Dx[13])
print("F internas: ")
print(solucion_14)

solucion_15 = np.linalg.solve(matriz, vector_15)
print("Para theta = " + str(theta[14]))
print("reacciones:")
print(Ax[14], Ay[14], Dx[14])
print("F internas: ")
print(solucion_15)

solucion_16 = np.linalg.solve(matriz, vector_16)
print("Para theta = " + str(theta[15]))
print("reacciones:")
print(Ax[15], Ay[15], Dx[15])
print("F internas: ")
print(solucion_16)

solucion_17 = np.linalg.solve(matriz, vector_17)
print("Para theta = " + str(theta[16]))
print("reacciones:")
print(Ax[16], Ay[16], Dx[16])
print("F internas: ")
print(solucion_17)

solucion_18 = np.linalg.solve(matriz, vector_18)
print("Para theta = " + str(theta[17]))
print("reacciones:")
print(Ax[17], Ay[17], Dx[17])
print("F internas: ")
print(solucion_18)

print()
print("máximos que puede tener cada una de las barras (AB,AD,AE,BC,BE,CE,DE): ")
print()
c = zip(solucion_1, solucion_2, solucion_3, solucion_4, solucion_5, solucion_6, solucion_7, solucion_9, solucion_10, solucion_11, solucion_12, solucion_13, solucion_14, solucion_15, solucion_16, solucion_17, solucion_18 )
for datos in c:
    if abs(max(datos)) >= abs(min(datos)):
        print(max(datos))
    elif  abs(min(datos)) >= abs(max(datos)):
        print(min(datos))

# Ejercico 2
import fnmatch
area = 1200
esfuerzo_admisible = 21
fuerza_maxima = area * esfuerzo_admisible / 1000

#for comparacion in str(solucion_1):
    #if str(fuerza_maxima) <= comparacion:
        # strsolucion_1 = str(solucion_1)
        # dominio = fnmatch.filter(strsolucion_1, comparacion)
        # strdominio = str(dominio)
        # posicion = strsolucion_1.index(strdominio)
        # if dominio in strsolucion_1:
            # print(dominio)

