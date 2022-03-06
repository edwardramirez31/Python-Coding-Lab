# EJERCICIO 8
# Obtener la serie de Fibonacci entre 0 y 50.

# 1. Definir dos variables
x, y = 0, 1

# 2. Imprimir el primer valor 
print(x)

# 3. Definir la condicion de ciclo
while y < 50:
    # 4. Mostrar la salida de la serie Fibonacci
    print(y)

    # 5. Se realiza el intercambio de valores de intercambio para obtener la secuencia
    x, y = y, x + y
