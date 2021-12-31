# C++
import matplotlib.pyplot as plt
import numpy as np

# True // False

number = 4

# SINTAXIS:
# 1. Keyword if
# 2. Expresion condicional
# 3. :
# 4. Indentado a la derecha va el bloque codigo
if number % 2 == 0:
    print("Su numero es par")
else:
    print("Su numero es impar")

while number % 2 == 0:
    print("Su numero es par")
    number = 1

# print(-5)
# print(-4)
# print(-3)
# print(-2)
# print(-1)
numero_negativo = -5

while numero_negativo < 0:
    print(numero_negativo)
    numero_negativo = numero_negativo + 1


# SINTAXIS
# 1. for keyword
# 2. variable de iteracion
# 3. keyword in
# 4. iterable (lista)
# 5. Dos puntos
# 6. Bloque de codigo indentado a la derecha

lista = [5, 4, 5, 1]

for numero in [5, 4, 5, 1]:
    print(numero ** 2)

mensaje = "Hola Mundo"

for letra in mensaje:
    if letra != " ":
        print(letra)

# input: ARCHIVO TXT
# 1. Leo el archivo: Use la funcion open()
archivo = open("mbox-short.txt")
# suma = 0
# cantidad_de_numeros = 0
numeros = []
# 2. Itero a traves de cada linea del archivo
for linea in archivo:
    # 3.Verificar si estoy en la linea que contiene el ratio de spam
    if linea.startswith("X-DSPAM-Confidence"):
        # 4. Extraer el numero que esta guardado en ese ratio
        elementos_de_la_linea = linea.split()
        numero = float(elementos_de_la_linea[-1])
        numeros.append(numero)
        # suma = suma + numero
        # cantidad_de_numeros = cantidad_de_numeros + 1
# OUTPUT: PROMEDIO
# 5. Evaluar el promedio
# sumar todos los elementos
# dividir en la cantidad de indicadores de spam
print(numeros)
suma = sum(numeros)
cantidad = len(numeros)

promedio = suma / cantidad

print(f"Su promedio de spam es: {promedio}")

# NUMPY: utilizamos pip
# pip install numpy jupyter matplotlib pandas sympy
# x ** 2
x = np.linspace(0, 10, 10000)
y = x ** 2
plt.plot(x, y)
plt.show()

# William Steven Acevedo Rueda8:00
# 2192059_william Acevedo (Benjumea)
# Tú8:00
# Buen día, en unos minutos empezamos mientras llegan los demás
# Vayan escribiendo su código y grupo para la asistencia
# Andres Felipe Bulla Reyes8:01
# 2193020_Andres Bulla (Benjumea)
# Mario Acevedo8:01
# 2172127_Mario Acevedo (Cotes D2)
# jonathan stiven rodriguez rincon8:02
# 2200269_Jonatan Rodríguez (Cotes D2)
# William Steven Acevedo Rueda8:02
# 2192059 (D3) benjumea
# Dadvinson Bonilla8:03
# 2180178_Dadvinson Bonilla (Cotes D2)
# juan camilo rios gonzalez8:03
# 2192057_Juan Camilo Rios (cotes J1)
# Naren Herrera8:03
# 2180158_Naren Herrera (Cotes D2)
# Ricardo Andres Galeano Beltran8:03
# 2194519 Ricardo Galeano (J1)
# EDWIN MANRIQUE CASTAÑEDA8:04
# Edwin Manrique Castañeda 2122884 ( J1)
# Catalina Suarez8:05
# María Catalina Suárez Granados 2180136 (J1)
# Andres Felipe Bulla Reyes8:05
# 2193020_Andres Bulla (Benjumea H1)
# jonathan stiven rodriguez rincon8:05
# El plazo para el reto se amplió? porque yo no encontre la carpeta de entregas en la semana 2
# JESSICA NATHALIA VARGAS RAVELO8:05
# 2160814_Jessica Vargas (Benjumea H1)
# Andres Banderas Uribe8:06
# 2184597-andres banderas
# Sebastian Parra8:06
# 2182737_Sebastian Parra (H1)
# Eusebio Ramirez8:06
# 2192099_Eusebio Ramirez
# omar pabon8:06
# Omar Yesid Pabon Pabon-2194042 (J1 Cotes)
# Natalia Amaya8:07
# Natalia Cristina Amaya Moreno 2184155 (J1)
# Mariam Cassiani8:07
# 2194509_Mariam Cassiani (D2 Cotes)
# Andrès Riaño8:08
# 2184146 - Andrés Felipe Riaño Ramírez (J1)
# karen vides8:17
# 2184609_KarenYusetVidesMartinez
# Joan Palomino8:20
# 2171151_Milton Joan Palomino Tapias
# Laura Díaz9:29
# 2190205_Laura Andrea Díaz Beltrán
# Santiago Sierra9:40
# 2190152_Julián Santiago Sierra Amado (H2)
