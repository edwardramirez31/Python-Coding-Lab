#1 CARGA MÁXIMA
from queue import PriorityQueue
import numpy as np
from sympy import *

#DATOS
esfuerzo_ultimo = 400
factor_seguridad_ultimo= 1.27
esfuerzo_fluencia_tension = 250
esfuerzo_fluencia_cortante = 145
factor_seguridad_fluencia = 1.24

#esfuerzos admisibles
esfuerzo_admisible_ultimo = esfuerzo_ultimo / factor_seguridad_ultimo
esfuerzo_admisible_tension = esfuerzo_fluencia_tension / factor_seguridad_fluencia
esfuerzo_admisible_cortante = esfuerzo_fluencia_cortante / factor_seguridad_fluencia

#área de los cables en mm^2
area_1 = 31.66921
#área de los pasadores en mm^2
area_2 = 126.6768

#POR COMPATIBILIDAD APARECEN LAS ECUACIONES

#W1 = (5 / 6) * (esfuerzo / factor_de_seguridad) * area   / FBD * (5 / 6)
#W2 = (1.0878) * (esfuerzo / factor_de_seguridad) * area  / FBC * (1.0878)
#W3 = (1.2964) * (esfuerzo / factor_de_seguridad) * area  / FBE * (1.2964)
#W4 = (0.83332) * (esfuerzo / factor_de_seguridad) * area / FAy * (0.83332)

W1 = (5 / 6)
W2 = 1.0878
W3 = 1.2964
W4 = 0.83332

Cables = np.array([W1, W2, W3]) #para el area 1
Pasadores = np.array([W1, W2, W3, W4]) #para el area 2

#Se remplazan los valores correspondientes para los cables
area1_por_W = area_1 * Cables
Fultimoc = area1_por_W * esfuerzo_admisible_ultimo
Ffluenciac = area1_por_W * esfuerzo_admisible_tension
FWcables = np.append(Fultimoc, Ffluenciac)

#Se remplazan los valores correspondientes para los pasadores
area2_por_W2 = area_2 * Pasadores
Fultimop = area2_por_W2 * esfuerzo_admisible_ultimo
Ffluenciap = area2_por_W2 * esfuerzo_admisible_cortante
FWpasadores = np.append(Fultimop, Ffluenciap)

Carga_W = np.append(FWcables, FWpasadores)
print()
print("La carga máxima W en Newtons es: " + str(min(Carga_W)))
print()
print()


#2 REACCIONES FUERZAS Y DEFORMACIONES
# FBC FBD FBE FAy

print("Suponiendo que la fuerza FAy va en dirección hacia abajo se resuelve el sistema.")

c = min(Carga_W)

matriz = np.array([
        [1.0878, 0, 0, 0],
        [0, 0.83333333, 0, 0],
        [0, 0, 1.2964, 0],
        [0, 0, 0, 0.41666],
    ])
vector = np.array([c, c, c, c])
solucion = np.linalg.solve(matriz, vector)

print("la solución de las fuerzas y reaacciones en Newtons es: ")
print("FBC: " + str(solucion[0]))
print("FBD: " + str(solucion[1]))
print("FBE: " + str(solucion[2]))
print("FAy: " + str(solucion[3]))

print()

#cálculo de deformaciones unitarias de los cables
# ε = (F * E) / A

fuerzas_cables = solucion[0:3]
for i in fuerzas_cables:
    ε = (fuerzas_cables ) / (area_1 * 200000)

print("las deformaciones unitarias de los cables son [mm/mm]: ")
print("εBC: " + str(ε[0]))
print("εBD: " + str(ε[1]))
print("εBE: " + str(ε[2]))















