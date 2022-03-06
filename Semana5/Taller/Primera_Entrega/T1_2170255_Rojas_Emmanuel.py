mi_codigo = str(2162277)
x = 0
for i in mi_codigo:
    sumar = int(i)
    x+=sumar
from cmath import *
from decimal import *
L = 0.2*x
#respecto al esfuerzo de fluencia
seguridad_fluencia = Decimal((0, (1, 2, 7), -2)) 
#respecto al esfuerzo ultimo
seguridad_ultimo =Decimal((0, (1, 3, 0, -2)))

permisisble_tension= 250/seguridad_fluencia 
permisible_compresion = 145/seguridad_fluencia 
permisible_ultimo= 400/seguridad_ultimo 

#Estatica
## 0 = Ax-FBC*cos(50) FBC*Cos(40)                        
## 0 =-Ay+FBD+FBD+FBC*cos(40)+FBC*cos(50)           
## 0 =-(l/2)*(W*l)+(l*FBE*Cos(50))+(l*FBC*cos(40))+(l*FBD)    

#Deformaciones
# cos(40) = cambio longitud BC / desplazamiento AB
# cos(50) = cambio longitud BE / desplzamiento AB
# de lo naterior obtenemos:      FBC = FBE(cos(40)/cos(50))                               

# de las ecuaciones
#  Ax = 0        FBD=-FBE(((cos(40)**2)/cos(50)) + cos(50)+lW/2)

