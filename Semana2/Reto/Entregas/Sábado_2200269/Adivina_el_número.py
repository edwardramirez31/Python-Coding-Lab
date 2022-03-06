print("Adivine el número entre 1 y 9")

#Importar el modulo random con el fin de generar números aleatorios 
import random as rd

#utilizar la función rd.randint(rango de números) para obtener números enteros aleatorios
A = rd.randint(1,9)
print(A)
Usuario = int(input("Ingrese su número:"))

#Crear un bucle con un condicional, el cual determine si el número del usuario es igual al que genera la función random
while Usuario != A:
    Usuario = int(input("Ingrese su número:"))
else:
    print("¡Bien adivinado!")
