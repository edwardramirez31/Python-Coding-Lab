# NECESITO LA EDAD DEL USUARIO PARA PRODUCIR LA EDAD QUE TENDRA EN EL SIGUIENTE AÑO

# INPUT: Edad de la persona ? Restricciones: edad > 0
# 1. Pedir la edad al usuario
while True:
    try:
        edad_del_usuario = int(input("Ingrese su edad: "))
        if edad_del_usuario > 0:
            break
        else:
            print("Ingrese una edad valida")
    except:
        print("Ingrese una edad valida")
# 2. Calcular la edad del usuario en el siguiente año (edad + 1)
edad_mas_uno = edad_del_usuario + 1
# 3. Mostrar el resultado al usuario
print("Su edad dentro de un año será: " + str(edad_mas_uno))
# OUTPUT: Edad de la persona + 1

