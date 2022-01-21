user_input = input("Ingrese la temperatura \n")
scale = user_input[-1] # Saco el ultimo caracter para saber si es F o C
temperature = float(user_input[:-1])
if (scale == "c") or (scale == "C"):
    print((temperature * 1.8) + 32)
else:
    print((temperature - 32.0) / 1.8)