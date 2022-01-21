# EJERCICIO 4 
# Escribir un programa que construya un patron de caracteres

# *
# **
# ***
# ****
# ****
# ****
# ***
# **
# *

# 1. Cantidad maxima de asteriscos
n=4

# 2. Definir la condicional (ciclo anidado)
for i in range(1,n+1):
    for j in range(i):
        # 3. Mostrar la salida del asterisco con un espacio y una linea para cada ciclo
        print("* ", end= "")
    print()

# 4. Mostrar la salida de la linea de la mitad
print("* "*n)

# 5. Definir la condicional para la segunda mitad del patron (devolver el ciclo anterior)
for i in range (n, 0, -1):
    for j in range (i):
        print("* ", end= "")
    print()
