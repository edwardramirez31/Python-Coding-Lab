# Numero binarios 
dato=(input("Ingrese una secuencia de numeros binarios separados por una coma: "))
lista=(dato.split(','))
salida=[]
for numerob in lista:
    binarioinv=numerob[::-1]
    ciclo=0
    dec=0
    for digito in binarioinv:
        predec=int(digito)*2**ciclo
        ciclo+=1
        int(predec)
        dec+=predec
    if(dec%5==0):
        salida.append(numerob)
sal1=(str(salida).replace("[","").replace("'","").replace("]",""))
print("Los numeros binarios divisibles en 5 son: ",sal1)