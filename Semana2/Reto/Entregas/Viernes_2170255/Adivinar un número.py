# Adivinar un número generado aleatoriamente entre 1 y 9
numero = int(input("¡Prueba tu suerte! Ingresa un numero entero entre 1 y 9: "))
from random import*
n = randint(1,9)
print("El número aleatorio es {}".format(n))
while numero != n:
    print("Sigue intentando")
    numero= int(input("Por favor ingrese un nuevo numero: "))
    n = randint(1,9)
    print("El número aleatorio es {}".format(n))
print("¡Acertaste!")