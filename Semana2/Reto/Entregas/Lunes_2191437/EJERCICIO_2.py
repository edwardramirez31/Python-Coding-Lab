# EJERCICIO 2
# Convertir de C a F y de F a C 

# 1. Pedir el numero al usuario
temperatura = input("Escriba la temperatura (ej. 22C, 71.6F) : ")

# 2. Leer los ultimos dos caracteres
escala = temperatura[-1:]

# 3. Definir la condicional
if escala == "C":
    # 4. Tomar solo el valor numerico de la temperatura para realizar la conversion
    temperatura_num = int(temperatura[:-1])
    
    # 5. Realizar la conversion
    fahrenheit = temperatura_num * (9/5) + 32

    # 6. Mostrar la salida acorde a mi condicion
    print("{} es equivalente a {} F".format(temperatura,fahrenheit))

elif escala == "F":

    temperatura_num = int(temperatura[:-1])

    celcius = (temperatura_num - 32) * (5/9)
    print("{} es equivalente a {} C".format(temperatura,celcius))

else:
    print ("Escriba un valor de temperatura valido")
