mi_codigo = str(2162277)
x = 0
for i in mi_codigo:
    sumar = int(i)
    x+=sumar

# datos material
esfuerzo_ultimo = 400 
esfuerzo_fluencia_traccion = 250 
esfuerzo_fluencia_corte = 145 
E = 200

# datos de los elementos
from cmath import *
theta = (40 * pi)/180
sigma = (50 * pi)/180  #bE
diametro_pasador = (1 / 2)*25.4
Area_pasador = pi*((diametro_pasador/2)**2)
longitud_cables = 1.5
diametro_cables = (1 / 4)*25.4
area_cables = pi* ((diametro_cables/2)**2)

from decimal import *
L = 0.2*x

#factores de seguridad
seguridad_fluencia = Decimal((0, (1, 2, 7), -2)) 
seguridad_ultimo =Decimal((0, (1, 3, 0), -2))

# esfuerzos peermisibles
permisisble_tension= 250/seguridad_fluencia 
permisible_compresion = 145/seguridad_fluencia 
permisible_ultimo= 400/seguridad_ultimo 

import sympy as sp
# equilibrio y desplazamientos
F, Ax, Ay, FBE, FBD, FBC, w,  = sp.symbols('F Ax Ay FBE FBD FBC w ')
Fx = FBE * cos(theta) + Ax - FBC * cos(sigma)                  
Fy = Ay + FBD + FBE*cos(sigma) - w*L + FBC*cos(theta)
Ma = -L/2 * w*L + L*FBC*cos(theta) + L*FBE*cos(sigma) + L*FBD 
BE_equivalencia = sp.Eq(FBE - FBD*cos(sigma),0)
BE_formula = cos(sigma)*FBD
BC_formula = FBD*cos(theta)
BC_equivalencia = sp.Eq(FBC - FBD*cos(theta),0)

Ma = sp.Eq(-L/2 * w*L + L*BC_formula*cos(theta) + L*BE_formula*cos(sigma) + L*FBD,0)
fBD = sp.solve(Ma)[0][FBD]

# fuerzas en los cables(en funcion de W)
Cable_BE = FBD*cos(sigma)
Cable_BC = FBD*cos(theta)
F_cables = [Cable_BC, fBD, Cable_BE]

# valor maximo de W
W_max_cable = []
for cable in F_cables:
    ez_normal = sp.Eq(( 400/seguridad_ultimo), F / area_cables,)
    W_cables = sp.solve(ez_normal)[0] 
    W_max_cable.append(W_cables)

W_max_pasador = []    
for cable in F_cables:
    ez_cortante = sp.Eq(( 145/seguridad_fluencia), F / Area_pasador,)
    W_pasador = sp.solve(ez_cortante)[0] 
    W_max_pasador.append(W_pasador)
    
W_max_final =W_max_cable + W_max_pasador
maxima_W = (min(W_max_final))/1000
print("El maximo valor que puede tomar W es de {}".format(maxima_W,)) 

# Reacciones
Fx = Ax - (fBD*cos(theta)) * cos(theta) * cos(sigma) + (fBD*cos(sigma))  
Ax = sp.solve(Fx)[0]
Fy = Ay + (fBD*cos(sigma))*cos(sigma) + fBD  + (fBD*cos(theta))*cos(theta) - w*L 
Ay = sp.solve(Fy)[0]
Fy_c_doble = fBD + fBD*cos(sigma) * cos(sigma) + fBD*cos(theta) * cos(theta) 
Fx_c_doble = fBD*cos(sigma) - fBD*cos(theta) * sin(theta)* sin(sigma) 
FB_apoyo= sp.sqrt((Fx_c_doble**2)+ (Fy_c_doble**2))
F_apoyos = [Ay, FB_apoyo]

# sustituyendo el valor de W
Ma = sp.Eq(L*FBD*cos(theta)*cos(theta) + L*FBD -L/2 * maxima_W*L + L*(FBD*cos(sigma))*cos(sigma),0)
BD =  sp.solve(Ma)[0]

def_BD = (BD*L) / (area_cables*E) 
F_BC = BD*cos(theta)
def_BC = (F_BC  * L) / (area_cables*E )
F_BE = BD*cos(sigma) 
def_BE = (F_BE* L) / (area_cables*E )
reaccion_Ay = -(BD  + BD*cos(theta)*cos(theta) + BD*cos(sigma)*cos(sigma) - maxima_W*L) 
print("reaccion Ay {} ".format(reaccion_Ay,))
print("fuerza BD {}, fuerza BC {}, fuerza BE {}".format(BD, F_BC, F_BE))
print("deformacion BD {}, deformacion BC {}, deformacion BE {}".format(def_BD, def_BC, def_BE))