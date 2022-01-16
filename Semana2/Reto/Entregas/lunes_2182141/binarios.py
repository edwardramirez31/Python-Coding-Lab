
lista = [input()]
convertdo = str(lista)
print (convertdo)

separados = convertdo.split(',')
print (separados)
print (len(separados))
listado = []
for i in range(len(separados)):
    elemento = separados[i]
    if elemento == "1010" :
        listado.append(elemento)
print(listado)