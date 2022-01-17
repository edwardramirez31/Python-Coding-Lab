
from ast import Expression
import numpy as np
import sympy as sp

# Unidades De Los Cables [m]
longitud_cables = 1.5
# Diámetro De Los Cables [Pulgadas]
diámetro_cables = 1 / 4
# Area De Los Cables [mm]
área_cables = np.pi * (diámetro_cables * 25.4 / 1000) ** 2 / 4
#Unidades de los Pasadores
# Diámetro De Los Pasadores [pulgadas]
diámetro_pasadores = 1 / 2
# Area De Los Pasadores [mm]
área_pasadores = np.pi * (diámetro_pasadores * 25.4 / 1000) ** 2 / 4

print("Codigo 2194039")
código = "2194039"
X = sum((int(i) for i in código))
## Longitud de la barra en metros
L = 0.2 * X

FS_fluencia = float(f"1.{X}")
FS_resistencia_última = float(f"1{X + 3}")

ángulo_BC = 40 * np.pi / 180
ángulo_BE = 50 * np.pi / 180

# Propiedades del material [MPa]
esfuerzo_último = 400
esfuerzo_fluencia_tracción = 250
esfuerzo_fluencia_compresión = 145
## Módulo de elasticidad [GPa]
E = 200

# Ecuaciones de equilibrio
Ax, Ay, BC, BD, BE, W = sp.symbols('Ax Ay BC BD BE W')

Fx = Ax - BC * sp.sin(ángulo_BC) + BE * sp.sin(ángulo_BE)
equilibrio_X = sp.Eq(Fx , 0)
equilibrio_X
print("ΣFx = ",Fx, "= 0")


Fy = Ay - W * L + BC * sp.cos(ángulo_BC) + BE * sp.sin(ángulo_BE) + BD
equilibrio_Y = sp.Eq(Fy , 0)
equilibrio_Y
print("ΣFy = ",Fy, "= 0")


M_a = - W * L ** 2 / 2 + BC * sp.cos(ángulo_BC) * L + BE * sp.cos(ángulo_BE) * L + BD * L
equilibrio_momentos = sp.Eq(M_a , 0)
equilibrio_momentos
print("Ma= ", M_a , "= 0")


# Ecua por Compatibilidad de desplazamientos
equivalencia_BC = sp.Eq(BC - BD * sp.cos(ángulo_BC), 0)
ecuación_equivalente_BC = BD * sp.cos(ángulo_BC)
equivalencia_BC
print("equivalencia_BC" , equivalencia_BC, "= 0")


equivalencia_BE = sp.Eq(BE - BD * sp.cos(ángulo_BE), 0)
ecuación_equivalente_BE = BD * sp.cos(ángulo_BE)
equivalencia_BE
print("equivalencia_BE",equivalencia_BE, "= 0")


# Ecua del equilibro de momentos calculamos BD
ecuación = sp.Eq(M_a.subs([(BC, ecuación_equivalente_BC), (BE, ecuación_equivalente_BE)]), 0)
ecuación
print(ecuación, "= 0")


BD_respecto_W = sp.solve(ecuación)[0][BD]
BD_respecto_W
print(BD_respecto_W)


F_BC = ecuación_equivalente_BC.subs(BD, BD_respecto_W)
F_BE = ecuación_equivalente_BE.subs(BD, BD_respecto_W)

Fuerzas_cables = [F_BC, BD_respecto_W, F_BE]
Fuerzas_cables
print("Fuerzas_cables", Fuerzas_cables)


w_max = []
for fuerza in Fuerzas_cables:
    # Esfuerzo normal [Cables]
    ecuación_esfuerzo_normal = sp.Eq(fuerza / área_cables, esfuerzo_último * 10 ** 6 / FS_resistencia_última)
    w_cables = sp.solve(ecuación_esfuerzo_normal)[0] / 1000
    # Cortante en los pasadores superiores
    ecuación_esfuerzo_cortante = sp.Eq(fuerza / área_pasadores, esfuerzo_fluencia_compresión * 10 **6 / FS_fluencia)
    w_pasadores = sp.solve(ecuación_esfuerzo_cortante)[0] / 1000
    w_max.append(w_cables)
    w_max.append(w_pasadores)

print("Carga distribuida máxima en los cables [kN / m]", w_cables)
min(w_max)

# Cortante doble en los apoyos de la barra
Ay_eq = Fy.subs([(BC, ecuación_equivalente_BC), (BE, ecuación_equivalente_BE), (BD, BD_respecto_W)])
Ay_respecto_W = sp.solve(sp.Eq(Ay_eq, 0))
Ay_respecto_W = Ay_respecto_W[0][Ay]
Ay_respecto_W
print(Ay_respecto_W)

Ax_eq = Fx.subs([(BC, ecuación_equivalente_BC), (BE, ecuación_equivalente_BE), (BD, BD_respecto_W)])
Ax_respecto_W = sp.solve(sp.Eq(Ax_eq, 0))
Ax_respecto_W = Ax_respecto_W[0][Ax]
Ax_respecto_W
print(Ax_respecto_W)

# Fuerza en el apoyo A
F_apoyo_A = sp.sqrt(Ay_respecto_W ** 2 + Ax_respecto_W ** 2)
F_apoyo_A
print("Fuerza en el apoyo A:", F_apoyo_A)

# Fuerza en la conexión de los cables
F_x_cortante_doble = ecuación_equivalente_BE.subs(BD, BD_respecto_W) * sp.sin(ángulo_BE) - ecuación_equivalente_BC.subs(BD, BD_respecto_W) * sp.sin(ángulo_BC)
F_y_cortante_doble = ecuación_equivalente_BE.subs(BD, BD_respecto_W) * sp.sin(ángulo_BE) + ecuación_equivalente_BC.subs(BD, BD_respecto_W)* sp.sin(ángulo_BC)
F_apoyo_B = sp.sqrt(F_x_cortante_doble ** 2 + F_y_cortante_doble ** 2)
F_apoyo_B
print(F_apoyo_B)

Fuerza_apoyos = [F_apoyo_A, F_apoyo_B]
w_max_apoyos = []
for fuerza in Fuerza_apoyos:
    ecuación_esfuerzo_cortante = sp.Eq(fuerza / área_pasadores, esfuerzo_fluencia_compresión * 10 ** 6 / FS_fluencia)
    w_pasadores = sp.solve(ecuación_esfuerzo_cortante) [0] / 1000
    w_max_apoyos.append(w_pasadores)
    

print("Carga distribuida máxima por pasadores [kN / m]")
carga_maxima = min(w_max)
carga_maxima
print("carga_maxima" , carga_maxima)

# CÁLCULO DE FUERZAS Y DEFORMACIONES

Fuerza_BE = ecuación_equivalente_BE.subs([(BD, BD_respecto_W), (W, carga_maxima)])
deformación_BE = (Fuerza_BE * 1000 * longitud_cables) / (área_cables * E * 10 ** 9)
# Fuerza [KN] y deformación [mm]
Fuerza_BE, deformación_BE * 1000
print("deformación_BE " , deformación_BE)
print("Fuerza_BE:" , Fuerza_BE)

Fuerza_BC = ecuación_equivalente_BC.subs([(BD, BD_respecto_W), (W, carga_maxima)])
deformación_BC = (Fuerza_BC * 1000 * longitud_cables) / (área_cables * E * 10 ** 9)
Fuerza_BC, deformación_BC * 1000
print("deformación_BC:" , deformación_BC)
print("Fuerza_BC:", Fuerza_BC)

Fuerza_BD = BD_respecto_W.subs(W, carga_maxima)
deformación_BD = (Fuerza_BD * 1000 * longitud_cables) / (área_cables * E * 10 ** 9)
Fuerza_BD, deformación_BD * 1000
print("deformación_BD:" , deformación_BD)
print("Fuerza_BD:", Fuerza_BD)

Valor_Ax = Fx.subs([(BE, Fuerza_BE), (BC, Fuerza_BC)])
Valor_Ax = sp.solve(sp.Eq(Valor_Ax, 0)) [0]
Valor_Ax
print("Valor_Ax:" , Valor_Ax)

Valor_Ay = Fy.subs([(BE, Fuerza_BE), (BC, Fuerza_BC), (BD, Fuerza_BD), (W, carga_maxima)])
Valor_Ay = sp.solve(sp.Eq(Valor_Ay, 0)) [0]
Valor_Ay
print("Valor_Ay: ", Valor_Ay)

