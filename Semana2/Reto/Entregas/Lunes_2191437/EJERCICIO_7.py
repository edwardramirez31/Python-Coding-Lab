# EJERCICIO 7
# Omitir valores
# imprimir del 0 al 6 omitiendo el 3 y 6

# 1. Difinir el bucle y rango de la lista que se va a revisar
for n in range(0, 7):
    # 2. Definir la condicion (3 y 6 multiplos de 3)
    if n % 3 != 0 or n == 0:
        print(n)
