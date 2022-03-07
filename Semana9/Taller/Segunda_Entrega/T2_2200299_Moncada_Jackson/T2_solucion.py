
from math import pi,cos,sin
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# EJERCICIO 1
#   1.a
# código"2200299"
X = 19
Y = X / 3

# longitudes [m]
L1 = 0.05 * X
L2 = L1 * 1.5
L3 = 0.5 * L1
L4 = L1 + L2 + L3

# Símbolos
x, Ay, MA = sp.symbols("x Ay MA")

# cargas [KN*m]
#tramo 2
W = 0.005 * X + 0.001 * Y
# tramo 1
W_t1 = (W/L1)*x
# tramo 3
W_t3 = (-W/L3)*x + W

#carga puntual [KN]
P = 0.05 * X
angulo = pi/4

# W puntuales # p = puntualizada la carga
W1 = (L1 * (W/2))
p1 = L1 * (2/3)

W2 = (L2 * W)
p2 = L1 + (L2/2)

W3 = (L3 * (W / 2))
p3 = L1 + L2 + L3/3

# Reaccion Ay (SF = sumatoria de fuerzas)
SF_y = Ay - (W1 + W2 + W3) + sin(angulo) * P
SFy = sp.Eq(SF_y, 0)
R = sp.solve(SFy)
Ay = R[0]
#print("Ay = " + str(Ay) + "[KN]")

# Momento MA [KN*m] (SM = sumatoria de momentos)
SM_A = MA - (W1*p1 + W2*p2 + W3*p3) + L4 * sin(angulo) * P
SMA = sp.Eq(SM_A, 0)
M = sp.solve(SMA)
MA = M[0]
#print("MA = " + str(MA) + "[KN*m]")

# Fuerzas internas

#Tramo 1
V_1 = -sp.integrate(W_t1, x) + Ay
V_1_L1 = V_1.subs(x,L1)

M_1 = sp.integrate(V_1, x) - MA
M_1_L1 = M_1.subs(x, L1)

#Tramo 2
V_2 = -sp.integrate(W, x) + V_1_L1
V_2_L2 = V_2.subs(x, L2)

M_2 = sp.integrate(V_2, x) - M_1_L1
M_2_L2 = M_2.subs(x, L2)

#Tramo 3
V_3 = -sp.integrate(W_t3, x) + V_2_L2
V_3_L2 = V_3.subs(x, L3)

M_3 = sp.integrate(V_2, x) - M_2_L2
M_3_L3 = M_3.subs(x, L3)

# Diagrama de cortante

x_array = np.arange(0, L4, 0.001)
tramo1 = sp.lambdify(x, V_1)(x_array[x_array < L1])
tramo2 = sp.lambdify(x, V_2)(x_array[(x_array >= L1) & (x_array < L1 + L2) ] - L1)
tramo3 = sp.lambdify(x, V_3)(x_array[(x_array >= L1+L2) & (x_array <= L4)] - L1 - L2)

plt.plot(x_array, np.concatenate((tramo1, tramo2, tramo3)))
plt.fill_between(x_array, np.concatenate((tramo1, tramo2, tramo3)), alpha=0.25)
plt.axvline(0, color="gray")
plt.axhline(0, color="gray")
plt.xlabel("X [m]")
plt.ylabel("F Cortante [kN]")
plt.title("Diagrama de cortante")

# Diagrama de Momento

x_array = np.arange(0, L4, 0.001)
tramo1 = sp.lambdify(x, M_1)(x_array[x_array < L1])
tramo2 = sp.lambdify(x, M_2)(x_array[(x_array >= L1) & (x_array < L1 + L2) ] - L1)
tramo3 = sp.lambdify(x, M_3)(x_array[(x_array >= L1+L2) & (x_array <= L4)] - L1 - L2)

plt.plot(x_array, np.concatenate((tramo1, tramo2, tramo3)))
plt.fill_between(x_array, np.concatenate((tramo1, tramo2, tramo3)), alpha=0.25)
plt.axvline(0, color="gray")
plt.axhline(0, color="gray")
plt.xlabel("X [m]")
plt.ylabel("Momento flector [kN*m]")
plt.title("Diagrama de momento")

# 1.b
# mayor cortante al final de la viga
Max_V = V_3.subs(x, L3)
# mayor momento al incio porque está empotrada
Max_M = M_1.subs(x, 0)
print("El mayor momento es " + str(Max_M) + " [KN*m] y el mayor cortante es " + str(Max_V) + " [Km]")

# EJERCICIO 2
#   2.a
import pandas as pd
from openpyxl import load_workbook

Esfuerzo_admisible = 250 # [MPa]
Esfuerzo_admi = -250

### tabla
perfiles = pd.read_excel("T2.xlsx", usecols ="B:E", skiprows = 3, nrows = 10, index_col="perfil")

### Áreas

A_1 = perfiles["t [mm]"] * perfiles["b [mm]"]
A_2 = (perfiles["h [mm]"] - perfiles["t [mm]"]) * perfiles["t [mm]"]
perfiles["A [mm^2]"] = A_1 + A_2

### Centroides

# centroide de la primer rectángulo
Y_1 = perfiles["h [mm]"] - (perfiles["t [mm]"] / 2)
# primer momento de area
AY_1 = A_1*Y_1

# centroide del segundo rectángulo
Y_2 = (perfiles["h [mm]"] - perfiles["t [mm]"]) / 2
# primer momento de area
AY_2 = A_2*Y_2

EN = (AY_1 + AY_2) / perfiles["A [mm^2]"]

### Inercias

I_1 = (perfiles["b [mm]"] * (perfiles["t [mm]"]) ** 3) / 12
#esteiner 1
S_1 = A_1 * (Y_1 - EN) ** 2

I_2 = (perfiles["t [mm]"] * (perfiles["h [mm]"] - perfiles["t [mm]"]) ** 3) / 12
#esteiner 1
S_2 = A_2 * (Y_2 - EN) ** 2

Iz = I_1 + S_1 + I_2 + S_2
perfiles["Iz [mm ^ 4]"] = Iz
perfiles["Eje neutro [mm]"] = EN

### Esfuerzos
# se multiplica el momento por 10**6 para que las unidades sean [N*mm]

E_sup = ((-Max_M * 10 ** 6) * (perfiles["h [mm]"] - perfiles["Eje neutro [mm]"])) / perfiles["Iz [mm ^ 4]"]
E_inf = ((Max_M * 10 ** 6) * perfiles["Eje neutro [mm]"]) / perfiles["Iz [mm ^ 4]"]

perfiles["Esfuerzo Inf [MPa]"] = E_inf
perfiles["Esfuerzo Sup [MPa]"] = E_sup

# Acomodar columnas de la tabla
perfiles = perfiles[["b [mm]", "h [mm]", "t [mm]", "A [mm^2]", "Iz [mm ^ 4]", "Eje neutro [mm]", "Esfuerzo Inf [MPa]", "Esfuerzo Sup [MPa]"]]

print(perfiles)

# perfíl mas óptimo

filtro = (perfiles["Esfuerzo Inf [MPa]"] <= Esfuerzo_admisible) & ( Esfuerzo_admi <= perfiles["Esfuerzo Sup [MPa]"])
perfiles_esfuerzo = perfiles[filtro]

indice = perfiles_esfuerzo.loc[filtro, "A [mm^2]"].idxmin()
perfil_optimo = perfiles.loc[[indice], ["b [mm]", "h [mm]", "t [mm]", "A [mm^2]", "Esfuerzo Inf [MPa]", "Esfuerzo Sup [MPa]"]]

print(perfil_optimo)

# Exportar

with pd.ExcelWriter('T2.xlsx', mode='a', engine='openpyxl') as writer:
    # configurando sheets
    book = load_workbook('T2.xlsx')
    # colocar el book dentro del writer de pandas
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    perfiles.to_excel(writer, startrow=3, startcol=6, sheet_name='perfiles', index=None)
    perfil_optimo.to_excel(writer, startrow=18, startcol=6, sheet_name="perfiles", index = None)


