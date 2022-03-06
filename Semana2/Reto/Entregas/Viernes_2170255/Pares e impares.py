# Pares e impares
lista = input("Ingrese una lista de numeros separados por una coma(,): ")
numeros =(lista.split(","))
pares=0
impares=0
for caracter in numeros:
    if int(caracter) %2 == 0:
        pares +=1
    elif int(caracter) %2 != 0:
        impares +=1
print("En su lista hay {} impares y {} pares".format(impares,pares))
