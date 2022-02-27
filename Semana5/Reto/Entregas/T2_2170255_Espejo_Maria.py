codigo = (input("Por favor ingrese su codigo de estudiante: "))
x = 0
for numero in codigo:
    sumar = int(numero)
    x+=sumar
# ya tengo el valor de mi x

import numpy as np
import sympy as sp

# DATOS
y = x/3
W_max = 0.005*x + 0.01*(y) 
p = 0.05*x
l1 = 0.05*x
l2 = 1.5*l1
l3 = 0.5*l1
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
# sumatoria de momentos en C 
Ma = Ay*(l1+l2) - P1*(l2+(l1/3)) - P2*(l2/2) + P3*(l3/3) - Py*l3 


# FUERZAS INTERNAS

# Tramo AB 0 < X <= l1
from sympy.abc import X
W_AB = (W_max*X)/l1 
V_AB = -(sp.integrate(W_AB,X)) + Ay
M_AB = Ma + sp.integrate(V_AB,X)

V_AB_Ev = V_AB.subs ({X: l1})
M_AB_Ev = M_AB.subs ({X: l1})

# Tramo BC 0 < X <= l2
W_BC = W_max
V_BC = -(sp.integrate(W_BC,X)) + V_AB_Ev
M_BC = (sp.integrate(V_BC,X)) + M_AB_Ev

V_BC_Ev = V_BC.subs ({X: l2})
M_BC_Ev = M_BC.subs ({X: l2})

# Tramo CD 0 < X <= l3
W_CD = (-W_max*X)/l3
V_CD = -(sp.integrate(W_CD,X)) + V_BC_Ev
M_CD = (sp.integrate(V_CD,X)) + M_BC_Ev

V_CD_Ev = V_CD.subs ({X: l3})
M_CD_Ev = M_CD.subs ({X: l3})

# Gráfica de cortante
import matplotlib.pyplot as plt

def tramo1(X):
    return(V_AB)
def tramo2(X):
    return(V_BC)
def tramo3(X):
    return(V_CD)
a=0
b=l1
c=l2
d=l3

X=np.linspace(a,d,500)
y = np.piecewise(X,[(a<=X) & (X<b), (b<=X) & (X<c), (c<=X) & (X<=d)],[lambda X:tramo1(X), lambda X:tramo2(X), lambda X:tramo3(X)])

tramo1 = np.vectorize(tramo1)
plt.plot([X<b],tramo1(X,[X<b]), label= "tramo 1")
plt.plot(X,([b<=X]&[X<c]),tramo2(X,([b<=X]&[X<c])), label= "tramo 2")              
plt.plot(X,[(c<=x) & (X<=d)],tramo3(X,[(c<=X) & (X<=d)]), label= "tramo 3")                

plt.grid(True)
plt.legend


    


