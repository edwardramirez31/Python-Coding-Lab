documento = input('Ingrese su documento: ')
separar = documento.split(".")
capitalizar = separar[-1]
resultado = capitalizar.capitalize() 
print('Su resultado es:', resultado)