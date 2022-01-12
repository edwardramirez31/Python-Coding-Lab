#Convertir de grados Celsius a Fahrenheit o viceversa
Celsius = int(input("Ingrese la cantidad de grados CELSIUS a convertir: "))
Fahrenheit = 1.8*Celsius+32
Fahrenheit_a = int(input("Ingrese la cantidad de grados FAHRENHEIT a convertir: "))
Celsius_a = Fahrenheit_a/1.8 - 17.77778

print(Celsius,"grados Celsius equivalen a",Fahrenheit,"grados Farenheit")
print(Fahrenheit_a, "grados Farenheit equivalen a",Celsius_a,"grados celsius")
