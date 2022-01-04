#Escriba un programa que acepte el nombre de un archivo por parte del usuario e imprima su extensión
#1. Se pide al usuario que ingrese el tipo de documento
Doc=input("ingrese el tipo de documento:")
#2. Se utiliza la funcción split para devoler una lista de cadenas
Doc=Doc.split('.') 
#3. En el paso anterior se separan las palabras y se imprime la ultima palabra de la expresión
#que corresponde a la extensión del archivo.
print((Doc[-1]))
