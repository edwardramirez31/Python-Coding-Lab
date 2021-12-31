Números = input("INSERTE NÚMEROS SEPARADOS POR COMAS:")
Lista = Números.split(",")
contador = 0
contador2 = 0
for i in Lista:
    if int(i) % 2 == 0:
        contador = contador + 1 
    else:
        contador2 = contador2 +1 
print(f"CANTIDAD DE NÚMEROS PARES:{contador}")
print(f"CANTIDAD DE NÚMEROS IMPARES:{contador2}")