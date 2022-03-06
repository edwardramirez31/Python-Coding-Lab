nombre = input('Escriba su nombre: ')
edad = int(input('Escriba su edad: '))
if edad < 100:
    año_100 = 2021 + (100 - edad)
    print(nombre, "a la edad de 100 años, estarás en el año "  + str(año_100))
elif edad == 100:
    año_100 = 2021
    print(nombre, "este es tu año 100!!! El "  + str(año_100))
else:
    print(nombre, 'alto ahí. No te hagas el gracioso.')