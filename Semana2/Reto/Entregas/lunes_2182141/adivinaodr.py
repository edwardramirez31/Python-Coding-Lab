import numpy as np
import random

numero = int(random.randrange(1,9,1))
print(numero)
print("advine el numero, igrese un valor de 1 a 9")
valor_usuario = int(input ())
if valor_usuario == numero:
    print("es es")
if valor_usuario != numero:
    print("ingrese otro")
    Newvalor_usuario = input()
    while int(Newvalor_usuario) !=numero:

            print("ingrese otro")
            Newvalor_usuario = input()
            
print(" ese es")
