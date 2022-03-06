print("ingrese el numero para hacer la tabla ")
numero = int(input())
print("la tabla es:")
for i in range (0,10):
    multiplicacion = (i+1) * numero
    print(str(i+1) + " x "+ str(numero) + " = " + str(multiplicacion) )

