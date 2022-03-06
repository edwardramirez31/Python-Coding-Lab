print("iingrese el texto")
texto = input()

numeros = 0
letras = 0
for i in texto :
    if i.isalpha():
        letras = letras + 1
    elif i.isdigit():
        numeros = numeros + 1

print("el texto ingresado tiene "+str(numeros)+" numeros")
print("el texto ingresado tiene "+str(letras)+" letras")