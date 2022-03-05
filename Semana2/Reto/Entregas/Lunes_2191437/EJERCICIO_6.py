# EJERCICIO 6
# Pares e impares en una lista

# 1. Definir la funcion del contador
def contar(lista):
    pares,impares = 0, 0 

    #2. Definir condicion para revisar cada numero en la lista
    for n in lista:
        if n % 2 == 0: 
            pares += 1
        else:
            impares += 1

    #3. Devolvemos la cantidad de pares e impares 
    return pares, impares

# 4. Definimos la lista de numeros
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. Definimos la variable que da el resultado de pares e impares
rtdo = contar(num)

# 6. Mostrar la salida de los pares e impares contados
print("La cantidad de pares es: %i" % rtdo[0])
print("La cantidad de impares es: %i" % rtdo[1])
