def contar(cadena):
    letras = []
    numeros = []

for x in cadena:
    if x.isdigit():
        numeros += 1
        numeros.append(x)
            
    elif x.isalpha ():
        letras += 1
    else:
        pass
    return digitos, letras

text_1 = input("Escriba el texto: ")


rtdo = contar(text_1)

print("La cantidad de digitos: %i" % rtdo[0])
print("La cantidad de letras: %i" % rtdo[1])




    
        
        