fibonacci = [0, 1]

for i in range(1, 49):next = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(next)
    #El comando append permite agregar elementos a la lista.
print (f'Los primeros 50 elementos de la serie Fibonacci son: {fibonacci}')