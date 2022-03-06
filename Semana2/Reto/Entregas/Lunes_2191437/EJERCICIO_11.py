# EJERCICIO 11
# Calcule el número de dígitos y letras.

# 1. Definir la funcion
def contar(cadena):

    #2. Crear variables
    digitos = 0
    letras = 0

    # 3. Definir la condicion
    for x in cadena:
        if x.isdigit ():
            digitos += 1
        elif x.isalpha ():
            letras += 1
        else:
            pass

    return digitos, letras

# 4. Pedir el texto al usuario 
text_1 = input("Escriba el texto: ")

# 5. Se crea una variable y se muestra la salida de acuerdo a las condiciones
rtdo = contar(text_1)

print("La cantidad de digitos: %i" % rtdo[0])
print("La cantidad de letras: %i" % rtdo[1])
