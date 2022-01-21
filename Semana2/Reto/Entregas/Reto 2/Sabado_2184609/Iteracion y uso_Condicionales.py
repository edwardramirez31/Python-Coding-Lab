## iterar y usar condiciones
for number in range(1500,2701): # se pone 20701 para que el ciclo incluya el 20700
    if (number % 5 == 0) or (number % 7 == 0):
        print(number)
