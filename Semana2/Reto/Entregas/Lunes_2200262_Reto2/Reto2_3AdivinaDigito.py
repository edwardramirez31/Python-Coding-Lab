#Adivinar un número de 1 a 9
print("Vamos a adivinar un número de 1 a 9")
Numero_min = 1
Numero_max = 9
import random
numero_aleatorio = random.randint(Numero_min,Numero_max)
numero_escogido = input("Selecciona un número entre" + " " + str(Numero_min) + " " +"y" + " " + str(Numero_max) )
#El comando random.randint selecciona un número aleatorio entre 1 y 9 en este caso, pues ya los seleccionamos.

if numero_escogido != numero_aleatorio:
    print(input("Selecciona un número entre" + " " + str(Numero_min) + " " +"y" + " " + str(Numero_max) ))  
if numero_escogido == numero_aleatorio:
    print("Bien adivinado")