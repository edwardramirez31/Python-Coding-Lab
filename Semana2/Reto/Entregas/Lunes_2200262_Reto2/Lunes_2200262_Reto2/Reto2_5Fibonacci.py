#Encontrar la serie de Fibonacci entre o y 50. Fibo = 0,1,1,2,3,5,8,21,...}

 #A partir de los 2 primeros números de la serie empezamos a iterar.
fibonacci = [0, 1]

for i in range(1, 49):
    #Sabemos que en la serie, el número siguiente es el anterior (i-1), + el actual (i)
    next = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(next)
    #El comando append permite agregar elementos a la lista.
print(f'Los primeros 50 elementos de la serie Fibonacci son: {fibonacci}')