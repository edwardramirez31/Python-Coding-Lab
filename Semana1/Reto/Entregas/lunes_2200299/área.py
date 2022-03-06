radio = float(input('Dijite el radio del círculo: '))
unidades = input('Dijite las unidades del radio: ')
unidades_de_área =  unidades + '^2'
from math import pi
área = pi * (radio**2)
print('El área del círculo es: ' + str(área ) + ' ' + unidades_de_área)