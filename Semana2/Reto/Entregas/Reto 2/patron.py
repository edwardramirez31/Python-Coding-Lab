
caracter = input("itroduzca un caracter: ")
n = int(input("introduzca el número de la fila más lárga del patrón:. "))

for i in range(1, n + 1):
    for x in range(i):
        print(caracter, end = " ")
    print()

for i in range(n - 1, 0, -1):
    for x in range(i):
        print(caracter, end = " ")
    print()


