
print("ingrese su contraseña")
contraseña = input()
cantidad = len(contraseña)
numeros = 0
letras = 0
mayusculas = 0
caracter = 0
for i in contraseña :
    if i.isalpha():
        letras = letras + 1

for i in contraseña :
    if i.isdigit():
        numeros = numeros + 1

for i in contraseña:
    if i.isupper():
        mayusculas = mayusculas + 1
for i in contraseña:
    if i == "$" or i=="#" or i=="@":
        caracter = caracter + 1

if letras>0 and mayusculas>0 and numeros >0 and caracter>0  and cantidad>=6 and cantidad <=15 :
    print ("contraseña valida")
else:
        print("contraseña invalida")