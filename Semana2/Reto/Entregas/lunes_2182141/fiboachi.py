from typing import final


lista = list(range(0,51))
print(lista)
fibonaciii = [0,1]
cantidad = len(lista)
for i in range(0, int(lista[-1])):
    numero = (fibonaciii[i]) + (fibonaciii[i+1])
    fibonaciii.append(numero)
print(fibonaciii) 
final = []
print(final)
cantidad = len(fibonaciii)
for i in range(0 , cantidad):
    num_final = (fibonaciii[i])
    if num_final <= 50 :
        final.append(num_final)
        
print(final)