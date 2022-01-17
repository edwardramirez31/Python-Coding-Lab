codigo = (input("Por favor ingrese su codigo de estudiante: "))
x = 0
for numero in codigo:
    sumar = int(numero)
    x+=sumar
# ya otuve el valor de mi x

from cmath import pi, sin
from decimal import *
l = 0.2*x # lingitud de mi barra
a=int(str(x)[0])
b=int(str(x)[1])
c= x+3
a2=int(str(c)[0])
b2=int(str(c)[1])

fs1 = Decimal((0, (1, a, b), -2)) #factor de seguridad respecto al esfuerzo de fluencia
fs2 =Decimal((0, (1, a2, b2), -2)) #factor de seguridad respecto al esfuerzo ultimo

ez_ten_permisibel1= 250/fs1 #esfuerzo permisible respecto al esfuerzo de fluencia a Tension
ez_com_permisible= 145/fs1 #esfuerzo permisible respecto al esfuerzo de fluencia a Compresion
ez_permisible2= 400/fs2 #esfuerzo permisible respecto al esfuerzo ultimo

#Analizando la estatica general
import math
from math import *
# sumatoria de fuerzas en x #   0 = Ax -FBC*cos(50) + FBC*Cos(40)                         Ecuacion 1
# sumatoria de fuerzas en y #   0 = -Ay + FBD + FBD + FBC*cos(40) + FBC*cos(50)           Ecuacion 2
# Momento en el punto A #       0 = -l/2 * Wl + l*FBC*cos(40) +l*FBD + l*FBE*Cos(50)      Ecuacion 3

#Analizando las deformaciones
# cos(40) = Cambio de longitud BC / desplazamiento de la barra rigida
# cos(50) = cambio de la longitud BE / desplzamiento de la barra rigida
# de lo naterior obtenemos:      FBC = FBE(cos(40)/cos(50))                               Ecuacion 4

# usando las 4 ecuaciones llego a:
# Ax = 0     FBD = lW/2 - FBE ( ((cos(40)**2)/cos(50)) + cos(50))

#Analizando el puto A 
# exfuerzo = F_interna / Area
Area_pasador = pi*((6.35)**2)
W = (ez_com_permisible * Decimal(Area_pasador) * 2)/Decimal(l)



