# NECESITO LA EDAD DEL USUARIO PARA PRODUCIR LA EDAD QUE TENDRÁ EL SIGUIENTE AÑO

# INPUT: Edad de la persona? restricciones: edad >0

#1.Pedir la edad del usuario

while True:
    try:
        edad_del_usuario= int(input("ingrese su edad: "))
        if edad_del_usuario > 0:
            break
        else:
            print("Ingrese una edad valida")
    except:
        print("Ingrese una edad valida")
# 2. Calcular la edad del usuario en el siguiente año (edad + 1)
edad_mas_uno = edad_del_usuario + 1
# 3. Mostrar el resultado al usuario

print("su edad será: " + str(edad_mas_uno))
#print(edad mas uno)
#OUTPUT: Edad de la persona + 1