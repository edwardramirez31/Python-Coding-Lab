#➢	Escriba un programa de Python que pida el radio de una esfera y calcule su volumen.
import math
#1. Solicitar al usuario que ingrese el radio de la esfera
r=int(input("Ingrese el radio de la esfera: "))
#2. Calcular el volumen de una esfera
Vol=4/3*math.pi*pow(r,3)
#3. Imprimir el resultado del área de la esfera
print("El volumen de la esfera de radio: " + str(r)+ " es: "  + str(Vol))