resultado = []
for i in range(0,51):
    elemento = i
    residuotres = elemento % 3
    residuocinco = elemento % 5
    if residuotres == 0 and residuocinco != 0:
        resultado.append("fizz")
    elif residuocinco == 0 and residuotres != 0 :
        resultado.append("buzz")
    elif residuocinco == 0 and residuotres == 0 :
        resultado.append("fizzbuzz")
    else:
        resultado.append(i)
print(resultado)