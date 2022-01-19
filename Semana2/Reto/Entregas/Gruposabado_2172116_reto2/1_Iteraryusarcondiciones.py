lista_numeros = range(1500,2701)

span = []
spam = []

for i in lista_numeros:
    if i % 5 == 0:
        span.append(i)
        continue
    if i % 7 == 0:
        spam.append(i)
print("los numeros multiplos de 5 son " + str(span))
print("los numeros multiplos de 7 son " + str(spam))








##

##

##