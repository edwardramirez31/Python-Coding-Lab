##
nombrearchivo = input("EL nombre del archivo es:  ")
##
extencion = nombrearchivo.split(".")
##
print("La extension del archivo es: " + repr(extencion[-1]))
