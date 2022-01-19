lista_numeros = range(1500,2701)
numeros_pares = []
numeros_impares = []

for i in lista_numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
        continue
    if i % 2 != 0:
        numeros_impares.append(i)

print("la cantidad de numeros pares son " + str(len(numeros_pares)))
print("la cantidad de numeros impares son " + str(len(numeros_impares)))

