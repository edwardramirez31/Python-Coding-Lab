# Invertir palabras
palabra = input("Por favor ingrese una palabra: ")
num_letras = len(palabra)
n=-1
for caracter in palabra:
    letra= palabra[n]
    if num_letras+n >= 0:
        print(letra,end=(""))
    n -= 1
