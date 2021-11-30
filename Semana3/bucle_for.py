# import numpy as np
# from math import cos, pi, sin, sqrt

# np.set_printoptions(suppress=True)

lista_numeros = [2, 4, 6, 1, 3]

# for numero in lista_numeros:
#     print(numero ** 2)


lista_numeros = range(11)
# calcular el cuadrado de numeros pares entre 0 y 10

for i in lista_numeros:
    if i % 2 == 0:
        print(i ** 2)

# INPUT: No necesito (nombre del archivo)
# 1. Leer el archivo
archivo = open("mbox-short.txt")

spam = []

for linea in archivo:
    if not linea.startswith("X-DSPAM-Confidence"):
        continue

    lista_string = linea.split()
    numero = float(lista_string[1])
    spam.append(numero)

promedio = sum(spam) / len(spam)
print(promedio)

# Lunes: 6-8pm, Viernes: 6-8pm, Jueves 6-8pm

# 0  1  2
# [3, 5, 6]
archivo.close()

# OUTPUT: Promedio de SPAM de mis correos

# [1, 2, 3, 4, ...., 15]
# CONTINUE: salta a la siguiente iteracion, todo lo que esta por debajo no se ejecuta
for i in range(1, 16):
    if i % 2 != 0:
        if i == 9 or i == 11:
            continue
        print(i)

# BREAK: Se sale completamente del bucle
for i in range(1, 16):
    if i % 2 != 0:
        print(i)
        if i == 9:
            break
