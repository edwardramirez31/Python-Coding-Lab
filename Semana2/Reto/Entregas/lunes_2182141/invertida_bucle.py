print("ingrese su palabra")
palabra_usario = str(input())
Numeroletras = len(palabra_usario)
print(Numeroletras)
invertida = []
for i in range(0,Numeroletras):
    invertida.append(palabra_usario[(Numeroletras - 1 - i)])
print (invertida)
corrida = "su palabra invertida es:  "
for i in range(0,Numeroletras):
    corrida = corrida + str(invertida[i])
    
print(corrida)