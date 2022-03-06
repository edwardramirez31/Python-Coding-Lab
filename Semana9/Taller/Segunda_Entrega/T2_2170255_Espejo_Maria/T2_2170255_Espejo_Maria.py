codigo = str(2170255)
x = 0
for numero in codigo:
    sumar = int(numero)
    x+=sumar
# ya tengo el valor de mi x

from logging import _STYLES
import numpy as np
import sympy as sp

# DATOS
y = x/3
W_max = 0.005*x + 0.01*(y) 
p = 0.05*x
l1 = 0.05*x
l2 = 1.5*l1
l3 = 0.5*l1
L = (l1+l2+l3)
angulo_p_Grados = 45 
angulo_p_Rad = (45 * np.pi)/180

# PUNTUALIZACION DE CARGAS
P1 = (l1*W_max)/2
P2 = l2*W_max
P3 = (l3*W_max)/2
Px = p*(sp.cos(angulo_p_Rad))
Py = p*sp.sin(angulo_p_Rad)

# ESTATICA

# sumatoria de fuerzas en y 
Ay = P1 + P2 + P3 - Py
# sumatoria de fuerzas en X 
Ax = -Px
# sumatoria de momentos en A 
Ma = P1*(2*l1/3) + P2*((l2/2)+l1) + P3*((l3/3)+l1+l2) - Py*(l1+l2+l3) 


# FUERZAS INTERNAS

# Tramo AB 0 < X <= l1
from sympy.abc import X
W_AB = (W_max*X)/l1 
V_AB = -(sp.integrate(W_AB,X)) + Ay
M_AB = -Ma + sp.integrate(V_AB,X)
V_AB_Ev = V_AB.subs ({X: 0})
M_AB_Ev = M_AB.subs ({X: 0})
V_AB_Ev2 = V_AB.subs ({X: l1})
M_AB_Ev2 = M_AB.subs ({X: l1})

# Tramo BC 0 < X <= l2
W_BC = W_max
V_BC = -(sp.integrate(W_BC,X)) + V_AB_Ev2
M_BC = (sp.integrate(V_BC,X)) + M_AB_Ev2
V_BC_Ev = V_BC.subs ({X: 0})
M_BC_Ev = M_BC.subs ({X: 0})
V_BC_Ev2 = V_BC.subs ({X: l2})
M_BC_Ev2 = M_BC.subs ({X: l2})

# Tramo CD 0 < X <= l3
pendiente = W_max/(-l3)
W_CD = pendiente*X + W_max 
V_CD = -(sp.integrate(W_CD,X)) + V_BC_Ev2 
M_CD = (sp.integrate(V_CD,X)) + M_BC_Ev2
V_CD_Ev = V_CD.subs ({X: 0})
M_CD_Ev = M_CD.subs ({X: 0})
V_CD_Ev2 = V_CD.subs ({X: l3})
M_CD_Ev2 = M_CD.subs ({X: l3})

# Grafica de cortante
import matplotlib.pyplot as plt
X =  np.arange(0, 3.4, 0.01)
tramo1 = lambda X: -0.0833333333333333*X**2 - 0.324067459305202
tramo2 = lambda X: -0.183333333333333*X - 0.424900792638536
tramo3 = lambda X: 0.166666666666667*X**2 - 0.183333333333333*X + 0.0504166666666666
y = np.piecewise(X, [X < l1, (X >= 0) & (X <= (l2)), X <= (l3)], [tramo1, tramo2, tramo3])
plt.plot(X, y)
plt.axhline(0)
plt.axvline(0)
plt.title( "Cortante")
plt.fill_between(X, y, alpha=0.25,  color = "pink")
plt.show()

# Grafica de momento
X =  np.arange(0, (L+0.01), 0.01)
tramo5 = lambda X: -0.0277777777777778*X**3 - 0.324067459305202*X + 1.76265178237383
tramo6 = lambda X: -0.0916666666666667*X**2 - 0.424900792638536*X + 1.36920535491589
tramo7 = lambda X: 0.0555555555555556*X**3 - 0.0916666666666667*X**2 + 0.0504166666666666*X + 0.418556547062305
y = np.piecewise(X, [X < l1, (X >= 0) & (X <= (l2)), X <= (l3)], [tramo5, tramo6, tramo7])
plt.plot(X, y)
plt.axhline(0)
plt.axvline(0)
plt.title( "Momento")
plt.fill_between(X, y, alpha=0.25, color = "pink")
plt.show()


##   Segunda parte del ejercicio   ##

import pandas as pd

Mmax = np.amax(y)
Mmin = np.amin(y)

perfiles = pd.read_excel(r'C:\Users\MAFE\Desktop\ExcelTaller2.xlsx', usecols="A:D", index_col='Perfil')

# Medidas
h = perfiles.loc[1,'h[mm]']
b = perfiles.loc[1,'b[mm]']
e = perfiles.loc[1,'e[mm]']
Area=b*e+(h-e)*e
area1=e**2-e*h
area2=b*e

# Calculo del eje neutro
y1=(h-e)/2
y2=h-(e/2)
Eje_Neutro=(area1*y1+area2*y2)/(area1+area2)

# Calculo de inercias
inercia1=((e*(h-e)**3)/12)+area1*(Eje_Neutro-y1)**2
inercia2=((b*e**3)/12)+area2*(Eje_Neutro-y2)**2
InerciaZ=inercia1+inercia2

# Ezfuerzo
Esfuerzo=(Mmax*10**6*Eje_Neutro)/InerciaZ

# Tabla Excel
Resultado=perfiles
Resultado['A[mm^2]']=perfiles['b[mm]']*perfiles['e[mm]']+(perfiles['h[mm]']-perfiles['e[mm]'])*perfiles['e[mm]']
Resultado['EjeN[mm]']=((perfiles['e[mm]'])**2-(perfiles['e[mm]']*perfiles['h[mm]'])*((perfiles['h[mm]']-perfiles['e[mm]'])/2)+(perfiles['b[mm]']*perfiles['e[mm]'])*(perfiles['h[mm]']-(perfiles['e[mm]']/2)))/((perfiles['A[mm^2]']))
Resultado['Iz[mm^4]']=((perfiles['e[mm]']/12)*(perfiles['h[mm]']-perfiles['e[mm]'])**3)+((perfiles['e[mm]'])**2-(perfiles['e[mm]']*perfiles['h[mm]']))*(perfiles['EjeN[mm]']-((perfiles['h[mm]']-perfiles['e[mm]'])/2))**2+((perfiles['b[mm]']/12)*(perfiles['e[mm]'])**3)+(perfiles['b[mm]']*perfiles['e[mm]'])*(perfiles['EjeN[mm]']-((perfiles['h[mm]'])-(perfiles['e[mm]']/2)))**2
Resultado['Esfuerzo_Comp[MPa]']=(Mmax*10**6*(perfiles['h[mm]']-perfiles['EjeN[mm]']))/perfiles['Iz[mm^4]']
Resultado['Esfuerzo_Tens[MPa]']=(Mmax*10**6*(perfiles['EjeN[mm]']))/perfiles['Iz[mm^4]']
print("Tabla con los valores para cada uno de los perfiles {}".format(Resultado))

# Perfil mas economico
filtro=Resultado['Esfuerzo_Tens[MPa]']<=250
Resultado.loc[filtro,'A[mm^2]']
MenorArea=Resultado.loc[filtro, 'A[mm^2]'].min()
Posicion=Resultado.loc[filtro, 'A[mm^2]'].idxmin()
PerfilEscogido=Resultado.loc[[Posicion], :'Esfuerzo_Tens[MPa]']
print("El perfil mas economico es: {} ".format(PerfilEscogido))








