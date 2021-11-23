# INPUT: Dato de entrada es el numero
# 1. Pedir el numero al usuario
numero_ingresado = int(input())
residuo = numero_ingresado % 2
# 2. Evaluar si es par o impar, usando el operador %
# and
# or
# not
if numero_ingresado < 0 and residuo == 0:
    # 3. Mostrar la salida acorde con mi condicion
    print("Su numero es par y es negativo")
elif residuo == 0:
    print("Su numero es par")
else:
    print("Su numero es impar")


# QUIERO MOSTRAR "Hi, world." 5 veces
contador = 0

if contador < 5:
    print("Hi, world.")

# BUCLE INFINITO: la condicion siempre es verdera en este caso
# while contador < 5:
#     print("Hi, world.")

# Mejor sobre escribo una variable para que la condición llegue a ser falsa en el momento en que contador sea 5
while contador < 5:
    print("Hi, world.")
    contador = contador + 1

# OUTPUT: "Su numero es par" o "Su numero es impar"
