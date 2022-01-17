
unidades = input("dijite 'C' si tiene unidades en Celcius o dijite 'F' si tiene unidades en Fahrenheit ")

while unidades != "C":
    if unidades == "F" or unidades == "C":
        break
    print("Error. Introduce la letra correspondiente y revisa que estén en mayúscula.")
    unidades = input("dijite 'C' si tiene unidades en Celcius o dijite 'F' si tiene unidades en Fahrenheit ")

if unidades == "F" or unidades == "C":
        cantidad_numerica = int(input("introduzca la cantidad "))

if unidades == "F":
    Celcius = (cantidad_numerica - 32) * 5/9
    print(str(cantidad_numerica) + " grados Fahrenheit equivalen a " + str(Celcius) + " grados Celcius")

if unidades == "C":
    Fahrenheit = (cantidad_numerica * 9/5) + 32
    print(str(cantidad_numerica) + " grados Celcius equivalen a " + str(Fahrenheit) + " grados Fahrenheit")
