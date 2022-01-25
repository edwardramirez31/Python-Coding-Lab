codigo = (input("Por favor ingrese su codigo de estudiante: "))

x = 0
for numero in codigo:
    sumar = int(numero)
    x+=sumar
# ya otuve el valor de mi x

from cmath import pi, sin
from decimal import *

# lingitud de mi barra
l = 0.2*x 

# propiedades material
ez_ultimo = 400 
ez_fluencia_traccion = 250 
ez_fluencia_corte = 145 
E = 200

a=int(str(x)[0])
b=int(str(x)[1])
c= x+3
a2=int(str(c)[0])
b2=int(str(c)[1])

#factor de seguridad respecto al esfuerzo de fluencia
fs1 = Decimal((0, (1, a, b), -2)) 

#factor de seguridad respecto al esfuerzo ultimo
fs2 =Decimal((0, (1, a2, b2), -2)) 


ez_ten_permisibel1= ez_fluencia_traccion/fs1  #esfuerzo permisible respecto al esfuerzo de fluencia a Tension
ez_com_permisible= ez_fluencia_corte/fs1   #esfuerzo permisible respecto al esfuerzo de fluencia a Compresion
ez_permisible2= ez_ultimo/fs2      #esfuerzo permisible respecto al esfuerzo ultimo

#Otros Datos importantes
l_cables = 1.5
diametro_cables = (1 / 4)*25.4
area_cables = pi* ((diametro_cables/2)**2)
diametro_pasador = (1 / 2)*25.4
Area_pasador = pi*((diametro_pasador/2)**2)
angulo_BC = (40 * pi)/180
angulo_BE = (50 * pi)/180

#Estatica
import sympy as sp
import math
from math import *

Ax, Ay, FBC, FBD, FBE, W, X = sp.symbols('Ax Ay FBC FBD FBE W X')

# sumatoria de fuerzas en x #  Ecuacion 1
Fx = Ax - FBC * cos(angulo_BE) + FBE * cos(angulo_BC)                       
# sumatoria de fuerzas en y #  Ecuacion 2
Fy = Ay + FBD  + FBC*cos(angulo_BC) + FBE*cos(angulo_BE) - W*l   
# Momento en el punto A #  Ecuacion 3 
Ma = -l/2 * W*l + l*FBC*cos(angulo_BC) +l*FBD + l*FBE*cos(angulo_BE)      

# por compatibilidad de desplazamientos
expresion_BC = FBD*cos(angulo_BC)
igualdad_BC = sp.Eq(FBC - FBD*cos(angulo_BC),0)
expresion_BE = FBD*cos(angulo_BE)
igualdad_BE = sp.Eq(FBE - FBD*cos(angulo_BE),0)

# BD en funcion de W (Usando la ecuacion 3)
Ma = sp.Eq(-l/2 * W*l + l*expresion_BC*cos(angulo_BC) +l*FBD + l*expresion_BE*cos(angulo_BE),0)
BD =  sp.solve(Ma)[0][FBD]

# fuerzas en los cables(en funcion de W)
Cable_BC = BD*cos(angulo_BC)
Cable_BE = BD*cos(angulo_BE)
F_cables = [Cable_BC, BD, Cable_BE]

# hallando el valor maximo de W
W_max_cables = []
if F_cables != 0:
    valor_ez_normal = sp.Eq(ez_permisible2, X / area_cables,)
    W_cables = sp.solve(valor_ez_normal)[0] / 1000
    W_max_cables.append(W_cables)

W_max_pasadores = []    
if F_cables !=0:
    valor_ez_cortante = sp.Eq(ez_com_permisible, X / Area_pasador,)
    W_pasadores = sp.solve(valor_ez_cortante)[0] / 1000
    W_max_pasadores.append(W_pasadores)

W_max_estructura = W_max_cables + W_max_pasadores
maxima_W = min(W_max_estructura)
unidades = (" KN/m")
print("El maximo valor que puede tomar W es de {} {}".format(maxima_W, unidades))

# Reacciones 
Fx = Ax - (BD*cos(angulo_BC)) * cos(angulo_BE) + (BD*cos(angulo_BE)) * cos(angulo_BC) 
Ax = sp.solve(Fx)[0]
Fy = Ay + BD  + (BD*cos(angulo_BC))*cos(angulo_BC) + (BD*cos(angulo_BE))*cos(angulo_BE) - W*l 
Ay = sp.solve(Fy)[0]

# fuerza en el punto de conexión de los cables
Fx_cortante2 = BD*cos(angulo_BE) * sin(angulo_BE) - BD*cos(angulo_BC) * sin(angulo_BC)
Fy_cortante2 = BD*cos(angulo_BE) * cos(angulo_BE) + BD*cos(angulo_BC) * cos(angulo_BC) + BD
FB_Bearing = sp.sqrt(Fx_cortante2**2 + Fy_cortante2**2)
F_apoyos = [Ay, FB_Bearing]

# fuerzas, deformaciones y reacciones
Ma = sp.Eq(-l/2 * maxima_W*l + l*expresion_BC*cos(angulo_BC) +l*FBD + l*expresion_BE*cos(angulo_BE),0)
BD =  sp.solve(Ma)[0]

fuerza_BD = BD
deformacion_BD = (fuerza_BD*l) / (area_cables*E) 
fuerza_BE = BD*cos(angulo_BE) 
deformacion_BE = (fuerza_BE* l) / (area_cables*E )
fuerza_BC = BD*cos(angulo_BC)
deformacion_BC = (fuerza_BC* l) / (area_cables*E )
reaccion_Ay = -(+ BD  + (BD*cos(angulo_BC))*cos(angulo_BC) + (BD*cos(angulo_BE))*cos(angulo_BE) - maxima_W*l)
print("En la barra solo hay una reaccion, la reaccion Ay tiene un valor de {} {}".format(reaccion_Ay, unidades))
print("{:^20} {:^20} {:^20}".format("Cable", "fuerzas (KN/m)", "deformaciones"))
print("{:^20} {:^20} {:^20}".format( "BD", fuerza_BD, deformacion_BD))
print("{:^20} {:^20} {:^20}".format( "BC", fuerza_BC, deformacion_BC))
print("{:^20} {:^20} {:^20}".format( "BE", fuerza_BE, deformacion_BE))
