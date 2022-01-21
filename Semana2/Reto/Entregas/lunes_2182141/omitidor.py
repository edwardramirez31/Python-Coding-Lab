from typing import final


lista = list(range(0,7))
print(lista)
final = []
cantidad = len(lista)
for i in range(0,int(lista[-1])):
    numero = lista[i]
    if numero != 3 :
        final.append(lista[i])
    else :
        continue
print (final)