filename = input("Escriba el nombre del archivo: ")
f_extns = filename.split(".")
print("La extensión del archivo es : " + repr(f_extns[-1]))
