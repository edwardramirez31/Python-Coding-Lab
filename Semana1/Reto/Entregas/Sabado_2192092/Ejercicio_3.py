#Escriba un programa que acepte el nombre y apellido del usuario y los imprima en orden inverso,
# con un espacio entre ellos
#1. Se pide al usuario que ingrese su nombre y apellido
nombre=input("Ingrese su nombre y apellido: ")
#2. Se imprime el nombre inverso del usuario 
print("Su Nombre al revés es: " + nombre[::-1])
