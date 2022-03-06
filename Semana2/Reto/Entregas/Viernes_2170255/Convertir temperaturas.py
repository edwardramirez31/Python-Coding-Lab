# Convertir temperaturas desde grados Celsius a Fahrenheit o al contrario
tem = input("Ingrese el valor de temperatura y su respectiva unidad (en mayuscula): ")
unidad = tem[-1]
num = tem[:-1]
if unidad == "F":
    celsius = (int(num) - 32)*(5/9)
    print("La temperatura en celsius es {}".format(celsius))
elif unidad == "C":
    fahrenheit = (int(num)*(9/5)) + 32
    print("La temperatura en Fahrenheit es {}".format(fahrenheit))