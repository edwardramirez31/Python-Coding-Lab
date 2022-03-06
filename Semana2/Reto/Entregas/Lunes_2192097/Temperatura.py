print("ingrese la temperatura seguido de una C si esta en celsius o F si esta en Fahrenheit")
Entrada=input()
Lo=len(Entrada)
La=int(Lo)-1
Temperatura=Entrada[0:La]
#print(Temperatura)
if Entrada.endswith('C'):
    Fahrenheit= (int(Temperatura)*1.8)+32
    print("Su temperatura en Fahrenheit es: "+ str(Fahrenheit)+'F')
else:
    Celsius= (int(Temperatura)-32)*0.555555555555556
    print("Su temperatura en Celsius es: "+ str(Celsius)+'°C')