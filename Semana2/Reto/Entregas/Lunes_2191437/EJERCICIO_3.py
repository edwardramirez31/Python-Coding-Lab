# EJERCICIO 3
# Adivina el numero del 1 al 9

# 1. Definir el numero a adivinar
import random
num_adivinar = random.randint(1,9)

# 2. Definir el bucle para que el programa continue hasta que el numero se adivine
while True: 
    
    # 3. Pedir el numero al usuario
    num = int(input("Ingresa un número :"))

    # 4. Definir la condicional
    if num == num_adivinar :
        print("¡Bien adivinado!")
        break
