# EJERCICIO 5
#  Invertir palabras con un bucle

# 1. Definir la funcion
def inv_palabra(palabra):
    #2. Definir variable
    rta= ""

    #3. Invertir la palabra de izquierda a derecha
    for c in range(len(palabra)-1, -1, -1):
        rta += palabra[c]
    return rta

# 4. Pedir la palabra al usuario
frase = input("Escriba una palabara :")

# 5. Mostrar la salida acorde a la palabara
print(inv_palabra(frase))
