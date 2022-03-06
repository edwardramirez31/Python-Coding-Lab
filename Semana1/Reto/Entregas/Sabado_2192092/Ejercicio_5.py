#➢	Desarrolle un software que reciba un número n (integer) y dé como resultado el valor n
#+	nn + nnn
#1. Se pide al usuario un numero n
n=int(input("Ingrese un numero n: "))
#2. Se realiza la respectiva operación 
Resultado=n+n*n+n*n*n
#3. Se imprime el resultado de la opereación solicitada
print("El resultador de la operación de n+ nn + nnn, es:",Resultado)