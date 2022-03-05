def contador_par_impar(lista):
    pares, impares = 0,0
    for i in lista:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


numeros = [1, 2, 3, 4, 5, 6, 7, 9, 10]
resultado = contador_par_impar(numeros)

print("La cantidad de pares es: %i " % resultado[0])
print("La cantidad de impares es: %i " % resultado[0])

