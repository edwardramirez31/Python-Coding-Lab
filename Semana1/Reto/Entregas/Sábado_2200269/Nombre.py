Nombre = input("INSERTE SU NOMBRE: ")
Apellido = input("INSERTE SU APELLIDO: ")

nombre = ""
for i in Nombre:
    nombre = i + nombre

apellido = ""
for u in Apellido:
    apellido = u + apellido

NA = nombre +" "+ apellido
print("NOMBRE COMPLETO AL REVÉS", NA)