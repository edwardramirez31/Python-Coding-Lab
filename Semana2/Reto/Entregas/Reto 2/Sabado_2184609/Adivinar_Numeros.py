import random

number = random.randrange(1,9)
guested = False
while not guested:
    user_input = int(input("Ingresa un numero"))
    if user_input is number:
        guested = True
        print("Bien adivinado")
