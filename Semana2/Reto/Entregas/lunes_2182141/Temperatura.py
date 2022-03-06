import numpy as np
import re
print("ingrese su temperatura ")
Temperatura = input()
tempeText = str(Temperatura)

if tempeText.endswith("c" or "C"):
    valor = [float(s) for s in re.findall(r'-?\d+\.?\d*', tempeText)]
    valor_numerico = valor[0]
    farenjei = ( 9/5 * float(valor_numerico)) + 32
    print("su temperatura en grados farenjei es igual a " +str(farenjei))
elif tempeText.endswith("f" or "F"):
    valor = [float(s) for s in re.findall(r'-?\d+\.?\d*', tempeText)]
    valor_numerico = valor[0]
    celcius = (float(valor_numerico)-32)/1.8
    print("su temperatura en grados celcius es igual a  " + str(celcius))
