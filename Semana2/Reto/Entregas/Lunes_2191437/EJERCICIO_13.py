# EJERCICIO 13.1 
# Imprimir el patron alfabetico "E"

# *****
# *
# *
# ****
# *
# *
# *****

# 1. Crear el ciclo para los asteriscos
for i in range(7):
    
    # 2. Definir las condiciones para las lineas de asteriscos
    if i == 0 or i == 6:
        # 3. Mostrar la salida de esa linea
        print("*" * 5, end="")

    elif i == 1 or i == 2 or i == 4 or i == 5:
        print("*", end="")
    
    else:
        print("*" * 4, end="")
    print()





# EJERCICIO 13.2 
# # Imprimir el patron de mario bross

#     # #
#    ## ##
#   ### ###
#  #### ####

# 1. Pedir el numero al usuario
n = int(input("Escriba el numero de renglones de renglones del patron de mario bross: "))

# 2. Crear el ciclo para los numerales
for i in range(n+1):
    
    # 2. Definir los espacios
    espacio = n - i

    # 3. Mostrar la salida segun las condiciones
    print (" " * espacio + "#" * i + " " + "#" * i)
