#Desarrolle un software que pida al usuario su nombre y su edad. Mostrar un mensaje que le diga a esa 
# persona el año en el que va a cumplir 100 años
#1. Se pide al usuario que ingrese el nombre, la edad y el año actual en el que se encuentr
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
año=int(input("Ingrese el año actual en el que se encuentra: "))

A=100-edad
Añof=A+año
print(nombre + " en " + str(Añof) + " cumplirá 100 años")
