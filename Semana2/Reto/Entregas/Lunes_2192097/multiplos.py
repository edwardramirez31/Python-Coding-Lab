# seleccionar el rango
print("En este codigo se necesita un rango para obtener los multiplos, por tanto: ")
print("escriba el primer valor")
V_inicial=int(input())
print("escriba el segundo valor")
V_final=int(input())

if  V_inicial>=V_final:
    print("ingrese un rango de datos valido")
else:
    Numero=V_inicial
    Residuo=Numero%5
    if Residuo ==0 and Numero<=V_final:
        lista=Numero
        Numero=V_inicial+1
#definir multiplos de 5
#definir multiplos de 7
#mostrarlos en conjunto 