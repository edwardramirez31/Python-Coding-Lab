# Encontrar los números que son múltiplos de 5 y 7, entre 1500 y 2700 (ambos incluidos)
n=1500
while n <= 2700:
    multiplo5 = n%5
    multiplo7 = n%7
    if multiplo5 == 0 and multiplo7 == 0:
        print(n)
    n += 1
print("Fin de los multiplos de 5 y 7")