#EJERCICIO 1: RADIO DEL CILCULO
radio1=float(input("Inserte el radio: "))
import math
pi=math.pi
area=pi*radio1**2
print("El area del circulo es: "+str(area))

#EJERCICIO 2: NOMBRE INVERTIDO
nombre1=input("Inserte su nombre por favor: ")
apellido1=input("Inserte su apellido por favor: ")
resultado=(apellido1[::-1]+" "+nombre1[::-1])
print("Resultado: "+resultado)

#EJERCICIO 3: FORMATO DEL DOCUMENTO
nombre_doc=input("Ingrese el nombre de su documento: ")
formato=(nombre_doc[-4:])
print("El formato de su documento es: "+formato.capitalize())

#EJERCICIO 4: NUMERO n




#EJERCICIO 5: VOLUMEN DE UNA ESFERA
radio2=float(input("Ingrese el radio de la esfera: "))
vol=pi*(4/3)*radio2**3
print("El volumen de su esfera es: "+str(vol))

#EJERCICIO 6: CUANDO CUMPLIRA 100 AÑOS
nombre2=input("Ingrese su nombre: ")
edad1=int(input("Ingrese su edad: "))
sol=100-edad1+2021
print(nombre2+" usted cumplira 100 años en el año "+str(sol))

