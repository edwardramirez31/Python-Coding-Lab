#Escriba un programa de Python que pida el radio del circulo de un usuario 
# y muestre su área como salida.
#1. Se importan las librerias de matematematicas 
import math
#2. Se íde el radio al usuario
radio=(float(input("Ingrese el radio: ")))
#3. Se realiza la opereación para hallar el área
Area=math.pi*pow(radio,2)
#4. Se imptrime el resultado del área del circulo
print("El area del circulo es: " + str(Area))