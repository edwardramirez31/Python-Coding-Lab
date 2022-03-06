#Número de dígitos y letras.
cadena = input("Ingrese una cadena de numeros y letras: ")
digito = 0
letra = 0
for caracter in cadena:
    if caracter.isdigit():
        digito += 1
    elif caracter.isalpha():
        letra += 1
print("Las letras ingresadas fueron {} y los digitos {}".format(letra,digito))
