lista_numeros = range(1,51)
numeros = []

for i in lista_numeros:
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    print(i)


