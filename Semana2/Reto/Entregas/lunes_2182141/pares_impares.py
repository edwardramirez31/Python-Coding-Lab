print("INGRESE el numero inicial")
inicial = int(input ())
print("ingrese el valor final de su serie")
final = int(input())
pares = []
impares = []
rango_usuario = []
for i in range(inicial,(final + 1)):
    numero =  i
    rango_usuario.append(numero)
print(rango_usuario)
cantidad = len(rango_usuario)
for i in range (0,cantidad):
    if (rango_usuario[i] % 2) == 0 :
        pares.append(rango_usuario[i])
    else :
        impares.append(rango_usuario[i])
print("hay " + str(len(pares)) + " numeros pares")
print("hay " + str(len(impares)) + " numeros impares")