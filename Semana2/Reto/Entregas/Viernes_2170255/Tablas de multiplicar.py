# Tablas de multiplicar
numero= int(input("Ingrese un numero entero: "))
print("Tabla del " + str(numero))
for i in range (11):
    valor = i*numero
    print("{} x {} = {}".format(i,numero,valor))