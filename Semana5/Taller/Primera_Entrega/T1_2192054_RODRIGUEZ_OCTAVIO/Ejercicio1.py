


import numpy as np
import sympy as sp

#Codigo de estudiante= 2192054
#X=2+1+9+2+0+5+4

X=22

#Datos del problema al reemplazar la X correspondiente.
longitud_cables=1.5
longitud_barra= X*0.2 #[metros]
factor_seguridadflu= 1.22
factor_Seguridadult= 1.25


#Datos-propiedades mecanicas del material.
esfuerzo_ultimo = 400  #[Mpa]
esfuerzo_fluencia_traccion = 250   #[Mpa]
esfuerzo_fluencia_cortante = 145   #[Mpa]
E=200 #[Gpa]

#Esfuerzos admisibles del problema.

esfuerzoadmi_ultimo= esfuerzo_ultimo/ factor_Seguridadult
esfuerzoadmi_traccion= esfuerzo_fluencia_traccion /factor_seguridadflu
esfuerzoadmi_cortante= esfuerzo_fluencia_cortante/ factor_seguridadflu

#Determinacion de angulos respecto a los cables.

angulo_BC = 40 * np.pi / 180
angulo_BE = 50 * np.pi / 180

#Diametros

Diametro_Pasadores = 1/2 #[pulgadas]
Diametro_Cable = 1/4 #[pulgadas]

#Calculo de Areas

Area_Pasadores = np.pi * ((Diametro_Pasadores/2) * 25.4 / 1000) ** 2 #mm2 
Area_Cables = np.pi * ((Diametro_Cable/2) * 25.4/ 1000) ** 2 #mm2

#Equilibrio General Externo.

Ax, Ay, BD, BC, BE, W = sp.symbols("Ax Ay BD BC BE W")

# Sumatoria de Fuerzas en Y   (Fy=0)

Fy = Ay - (W * longitud_barra) + BD + (BE * sp.cos(angulo_BE)) + (BC * sp.cos(angulo_BC))
sumatoria_Fy = sp.Eq(Fy, 0)
sumatoria_Fy

# Sumatoria de Fuerzas en X  (Fx=0)

Fx = Ax + (BE * sp.sin(angulo_BE)) - (BC * sp.sin(angulo_BC))
sumatoria_Fx = sp.Eq(Fx, 0)
sumatoria_Fx

#Sumatoria de momentos respecto al punto A.  (Ma=0)

Ma = - W * (longitud_barra ** 2) / 2 + longitud_barra * BD + longitud_barra * BE * sp.cos(angulo_BE) + longitud_barra * BC * sp.cos(angulo_BC)
sumatoria_Ma = sp.Eq(Ma, 0)
sumatoria_Ma 

#Desplazamientos en los cables y relacion en los mismos.

#Relaciones geometrias entre BC-BD
relacion_BC = sp.Eq(BC - BD * sp.cos(angulo_BC), 0)
expresion_relacion_BC = BD * sp.cos(angulo_BC)
relacion_BC

#Relaciones geometrias entre BE-BD

relacion_BE = sp.Eq(BE - BD * sp.cos(angulo_BE), 0)
expresion_relacion_BE = BD * sp.cos(angulo_BE)
relacion_BE

#Reemplazar en equilibrio de momentos para obtener BD

ecuacion_reemplazada = sp.Eq(Ma.subs([(BC, expresion_relacion_BC), (BE, expresion_relacion_BE)]), 0)
ecuacion_reemplazada

#Solve de la ecuacion resultante. Encontramos BD en funcion de la carga W.

BD_vs_W = sp.solve(ecuacion_reemplazada)[0][BD]
BD_vs_W




#Resumen de Fuerzas.

Fuerza_BC = expresion_relacion_BC.subs(BD, BD_vs_W)
Fuerza_BE = expresion_relacion_BE.subs(BD, BD_vs_W)

vector_fuerzas_cables = [Fuerza_BC, BD_vs_W, Fuerza_BE]
vector_fuerzas_cables

#Calculo de W max en conjunto para cables.
Wmax = []
for fuerza in vector_fuerzas_cables:
    
    #Esfuerzo normal en los cables cables
    Ecuacion_esfuerzo_normal = sp.Eq(fuerza / Area_Cables, 400 * 10 ** 6 / factor_Seguridadult)
    W_cables = sp.solve(Ecuacion_esfuerzo_normal)[0] / 1000
    
    #Esfuerzo cortante simple en pasadores superiores.
    Ecuacion_esfuerzo_cortante = sp.Eq(fuerza / Area_Pasadores, 145 * 10 ** 6 / factor_seguridadflu)
    W_pasadores = sp.solve(Ecuacion_esfuerzo_cortante)[0] / 1000
    Wmax.append(W_cables)
    Wmax.append(W_pasadores)
    
print("Carga distribuida máxima en los cables [kN / m]")
min(Wmax)

#Ya tenemos la carga distribuida maxima en los cables, procedemos al calculo con los pasadores inferiores.


# Analisis del cortante doble en el apoyo A de la barra.

#Reaccion Ay
Reaccion_Ay_eq = Fy.subs([(BC, expresion_relacion_BC), (BE, expresion_relacion_BE), (BD, BD_vs_W)])
Reaccion_Ay_vs_W = sp.solve(sp.Eq(Reaccion_Ay_eq, 0))
Reaccion_Ay_vs_W = Reaccion_Ay_vs_W[0][Ay]
Reaccion_Ay_vs_W

#Reaccion Ax
Reaccion_Ax_eq = Fx.subs([(BC, expresion_relacion_BC), (BE, expresion_relacion_BE), (BD, BD_vs_W)])
Reaccion_Ax_vs_W = sp.solve(sp.Eq(Reaccion_Ax_eq, 0))
Reaccion_Ax_vs_W = Reaccion_Ax_vs_W[0][Ax]
Reaccion_Ax_vs_W

#Fuerza resultante en el apoyo A.

Fuerza_Apoyo_A = sp.sqrt(Reaccion_Ay_vs_W ** 2 + Reaccion_Ax_vs_W ** 2)
Fuerza_Apoyo_A

#Cortante generado en la union de los cables.

F_x_CortanteDoble = expresion_relacion_BE.subs(BD, BD_vs_W) * sp.sin(angulo_BE) - expresion_relacion_BC.subs(BD, BD_vs_W)
F_x_CortanteDoble = expresion_relacion_BE.subs(BD, BD_vs_W) * sp.sin(angulo_BE) - expresion_relacion_BC.subs(BD, BD_vs_W)
F_y_CortanteDoble = expresion_relacion_BE.subs(BD, BD_vs_W) * sp.cos(angulo_BE) - expresion_relacion_BC.subs(BD, BD_vs_W)
Fuerza_Apoyo_B= sp.sqrt(F_x_CortanteDoble ** 2 + F_y_CortanteDoble ** 2)
Fuerza_Apoyo_B


#Ahora calculamos la carga maxima en los pasadores similar a lo que hicimos para los cables.

vectorfuerza_apoyos = [Fuerza_Apoyo_A, Fuerza_Apoyo_B]
w_max_apoyos = []
for fuerza in vectorfuerza_apoyos:
    Ecuacion_esfuerzo_cortante = sp.Eq(fuerza / Area_Pasadores, esfuerzo_fluencia_cortante * 10 ** 6 / factor_seguridadflu)
    w_pasadores = sp.solve(Ecuacion_esfuerzo_cortante)[0] / 1000
    w_max_apoyos.append(w_pasadores)

print("Carga distribuida máxima por pasadores [kN / m]")
carga_maxima = min(Wmax)
carga_maxima

#Calculo de reacciones, Fuerzas y deformaciones correspondientes

#Cable BD

ValorResult_BD = BD_vs_W.subs(W, carga_maxima)
Deformacion_BD = (ValorResult_BD * longitud_cables) / (Area_Cables * E * 1000)
print("La fuerza del cable BD es de " + str(ValorResult_BD) + " kN")
print("La deformación del cable BD es de " + str(Deformacion_BD) + " mm")

# Cable BC

ValorResult_BC = expresion_relacion_BC.subs(BD, BD_vs_W)
W_BC = ValorResult_BC.subs(W, carga_maxima)
Deformacion_BC = (W_BC * longitud_cables) / (Area_Cables * E * 1000)
print("La fuerza del cable BC es de " + str(W_BC) + " kN")
print("La deformación del cable BC es de " + str(Deformacion_BC) + " mm")

# Cable BE
ValorResult_BE = expresion_relacion_BE.subs(BD, BD_vs_W)
W_BE = ValorResult_BE.subs(W, carga_maxima)
Deformacion_BE = (W_BE * longitud_cables) / (Area_Cables * E* 1000)
print("La fuerza del cable BE es de " + str(W_BE) + " kN")
print("La deformación del cable BE es de " + str(Deformacion_BE) + " mm")


#Calculo de reaccion en A-.

Reaccion_Ax = Reaccion_Ax_eq .subs([(BE, ValorResult_BE), (BC, ValorResult_BC)])
Reaccion_Ax = sp.solve(sp.Eq(Reaccion_Ax, 0))[0]
Reaccion_Ax

#El valor mostrado es la reaccion del punto A en direccion X.


Reaccion_Ay = Reaccion_Ay_eq .subs([(BE, ValorResult_BE), (BC, ValorResult_BC), (BD, ValorResult_BD), (W, Wmax)])
Reaccion_Ay = sp.solve(sp.Eq(Reaccion_Ay, 0))[0]
Reaccion_Ay

#El valor mostrado es la reaccion del punto A en direccion Y.
