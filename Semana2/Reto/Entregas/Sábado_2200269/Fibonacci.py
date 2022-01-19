#Crear una lista vacia para agrupar los valores de la secuencia
Lista = []

#Definir un bucle con condicionales para lograr obtener las entradas necesarias de la lista
for i in range(0,51):
    if i <= 1:
        Lista.append(i)
    
    elif i >= 2:
        #Para este caso resulta conveniente usar la función de obtener un dato especifico dentro de una lista
        #Sabemos que una nueva entrada dentro de la secuencia es el resultado de la suma de las dos anteriores
        X = Lista[i-1] + Lista[i-2]
        Lista.append(X)

print(Lista)      

