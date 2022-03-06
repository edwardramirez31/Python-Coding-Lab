#Crear una lista vacia para incluir los múltiplos de 5 y 7
Múltiplos = []

#Crear un bucle en el rango que se me pide y que cumpla con las condiciones dadas
for i in range(1500,2701):
    M5 = i % 5
    M7 = i % 7
    if M5 == 0 and M7 == 0:
        Múltiplos.append(i)

print(f"Múltiplos de 5 y 7: {Múltiplos}") 