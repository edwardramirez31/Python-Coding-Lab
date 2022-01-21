# EJERCICIO 1
# Encontrar los numeros que son multiplos de 5 y 7 entre 1500 y 2700

# 1. Definir las listas que contendran los valores 
def multiplos (limite_inferior, limite_superior):

    # 2. Evaluar si es multiplo de 5 y 7  
    if limite_superior > limite_inferior:
    
        resultado = []

        for n in range(limite_inferior, limite_superior+1):
            if n % 5 == 0 and n % 7 == 0:
               resultado.append(n)

        return resultado 

    #. raise ValueError("El limite inferior debe ser menor al limite superior.")

# 3. Definir el bucle o rango de la lista
numeros = multiplos(1500, 2700)

#4. Imprimir el resultado
print(numeros)
