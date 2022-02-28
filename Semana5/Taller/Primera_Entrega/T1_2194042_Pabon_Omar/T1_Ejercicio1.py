
import numpy as np
import sympy as sp

# 1.0 UNIDADES 
# 1.1 METROS
longitud_cables = 1.5
# 1.2 PULGADAS
diametro_cables = 1 / 4
# 1.3 MILIMETROS CUADRADOS
area_cables = np.pi * (diametro_cables * 25.4 / 1000) ** 2 / 4
# 1.4 PULGADAS
diametro_pasadores = 1 / 2
# 1.5 MILIMETROS CUADRADOS
area_pasadores = np.pi * (diametro_pasadores * 25.4 / 1000) ** 2 / 4

Codigo = "2194042"
x = sum([int(i) for i in Codigo]) 
# BARRA EN METROS
L = 0.2 * x

FS_fluencia = float(f"1.{x}")
FS_resistencia_Ult = float(f"1{x + 3}")

angulo_BC = 40 * np.pi / 180
angulo_BE = 50 * np.pi / 180

# PROPIEDADES DEL MATERIAL
# UNIDADES EN MPa
esfuerzo_ultimo = 400
esfuerzo_fluencia_tracion = 250
esfuerzo_fluencia_compresion = 145
# GPa
E = 200


# SUMATORIA DE FUERZAS EN Y AND X
Ax , Ay , BC , BD , BE , W = sp.symbols('Ax Ay BC BD BE W')
# SUMATORIA EN X
Fx = Ax - BC * sp.sin(angulo_BC) + BE * sp.sin(angulo_BE)
equilibrio_X = sp.Eq(Fx, 0)
equilibrio_X
print(equilibrio_X)

# SUMATORIA EN Y
Fy = Ay - W * L + BC * sp.cos(angulo_BC) + BE * sp.cos(angulo_BE) + BD
equilibrio_Y = sp.Eq(Fy, 0)
equilibrio_Y


# SUMATORIA DE MOMENTO
M_a = W * L **2 / 2 + BC * sp.cos(angulo_BC) * L + BE * sp.cos(angulo_BE) * L + BD * L
equilibrio_momento = sp.Eq(M_a, 0)
equilibrio_momento


# ECUACION DE COMPATIBILIDAD POR DESPLAZAMIENTO
igualando_BC = sp.Eq(BC - BD * sp.cos(angulo_BC), 0)
ecuacion_igualacion_BC = BD * sp.cos(angulo_BC)
igualando_BC

igualando_BE = sp.Eq(BE - BD * sp.cos(angulo_BE), 0)
ecuacion_igualacion_BE = BD * sp.cos(angulo_BE)
igualando_BE

# DESPEJAR BD DE LA SUMATORIA DE MOMENTO
ecuacion = sp.Eq(M_a.subs([(BC, ecuacion_igualacion_BC), (BE, ecuacion_igualacion_BE)]), 0)
ecuacion


BD_vs_W = sp.solve(ecuacion)[0][BD]
BD_vs_W


F_BC = ecuacion_igualacion_BC.subs(BD, BD_vs_W)
F_BE = ecuacion_igualacion_BE.subs(BD, BD_vs_W)

fuerza_cables = [F_BC, BD_vs_W, F_BE]
fuerza_cables

w_max = []
for fuerza in fuerza_cables:
    # ESFUERZO AXIAL DE LOS CABLES
    ecuacion_esfuerzo_axial = sp.Eq(fuerza / area_cables, esfuerzo_ultimo * 10 ** 6 / FS_resistencia_Ult)
    w_cables = sp.solve(ecuacion_esfuerzo_axial)[0] / 1000
    # PARA LOS PASADORES SUPERIORES EN CORTANTE SIMPLE
    ecuacion_esfuerzo_cortante = sp.Eq(fuerza / area_pasadores, esfuerzo_fluencia_compresion * 10 ** 6 / FS_fluencia)
    w_pasadores = sp.solve(ecuacion_esfuerzo_cortante)[0] / 1000
    w_max.append(w_cables)
    w_max.append(w_pasadores)

print("carga distribuida maxima en los cables [kN / m]", w_cables)
min(w_max)

# PARA LOS APOYOS EN CORTANTE DOBLE
Ay_eq = Fy.subs([(BC, ecuacion_igualacion_BC), (BE, ecuacion_igualacion_BE), (BD, BD_vs_W)])
Ay_vs_w = sp.solve(sp.Eq(Ay_eq, 0))
Ay_vs_w = Ay_vs_w[0][Ay]
Ay_vs_w
print(Ay_vs_w)

Ax_eq = Fx.subs([(BC, ecuacion_igualacion_BC), (BE, ecuacion_igualacion_BE), (BD, BD_vs_W)])
Ax_vs_w = sp.solve(sp.Eq(Ax_eq, 0))
Ax_vs_w = Ax_vs_w[0][Ax]
Ax_vs_w
print(Ax_vs_w)


# LAS FUERZAS EN EL APOYO A
F_apoyo_A = sp.sqrt(Ay_vs_w ** 2 + Ax_vs_w ** 2)
F_apoyo_A
print(F_apoyo_A)

# FUERZA DE CONEXION DE LOS CABLES EN EL PUNTO 
F_x_cortante_doble = ecuacion_igualacion_BE.subs(BD, BD_vs_W) * sp.sin(angulo_BE) - ecuacion_igualacion_BC.subs(BD, BD_vs_W) * sp.sin(angulo_BC)
F_y_cortante_doble = ecuacion_igualacion_BE.subs(BD, BD_vs_W) * sp.sin(angulo_BE) + ecuacion_igualacion_BC.subs(BD, BD_vs_W)* sp.sin(angulo_BC)
F_apoyo_B = sp.sqrt(F_x_cortante_doble * 2 + F_y_cortante_doble * 2)
F_apoyo_B
print(F_apoyo_B)


fuerzas_apoyo = [F_apoyo_A, F_apoyo_B]
w_max_apoyo = []
for fuerza in fuerzas_apoyo:
    ecuacion_esfuerzo_cortante = sp.Eq(fuerza / area_pasadores, esfuerzo_fluencia_compresion * 10 ** 6 / FS_fluencia)
    w_pasadores = sp.solve(ecuacion_esfuerzo_cortante)[0] / 1000
    w_max_apoyo.append(w_pasadores)

print("carga distribuida maxima por pasadores (kN / m",)
carga_maxima = min(w_max)
carga_maxima
print(carga_maxima)


# CALCULO DE FUERZAS Y DEFORMACIONES

valor_BE = ecuacion_igualacion_BE.subs([(BD, BD_vs_W), (W, carga_maxima)])
deformacion_BE = (valor_BE * 1000 * longitud_cables) / (area_cables * E * 10 ** 9)
# FUERZA EN kN y DEFORMACION mm
valor_BE, deformacion_BE * 1000
print(deformacion_BE)
print(valor_BE)

valor_BC = ecuacion_igualacion_BC.subs([(BD, BD_vs_W),(W, carga_maxima)])
deformacion_BC = (valor_BC * 1000 * longitud_cables) / (area_cables * E * 10 ** 9)
valor_BC, deformacion_BC * 1000
print(valor_BC)
print(deformacion_BC)

valor_BD = BD_vs_W.subs(W, carga_maxima)
deformacion_BD = (valor_BD * 1000 * longitud_cables) / (area_cables * E * 10 ** 9)
valor_BD, deformacion_BD * 1000
print(valor_BD)
print(deformacion_BD)

valor_Ax = Fx.subs([(BE, valor_BE), (BC, valor_BC)])
valor_Ax = sp.solve(sp.Eq(valor_Ax, 0))[0]
valor_Ax
print(valor_Ax)

valor_Ay = Fy.subs([(BE, valor_BE), (BC, valor_BC), (BD, valor_BD), (W, carga_maxima)])
valor_Ay = sp.solve(sp.Eq(valor_Ay, 0))[0]
valor_Ay
print(valor_Ay)










