lista_numeros = range(0, 234)
numeros = []

for i in lista_numeros:
    if i % 3 == 0 or i % 6 == 0:
        continue
    if i % 1 == 0:
        numeros.append(i)

print("los numeros son " + str(numeros))
