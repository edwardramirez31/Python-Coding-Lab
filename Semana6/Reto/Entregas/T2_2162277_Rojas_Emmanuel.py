codigo=(input("Ingrese su codigo: "))
x=0
for numero in codigo:
    suma=int(numero)
    x+=suma

import numpy as np
import sympy as sp

y=x/3
W=0.005*x+0.01*y 
p=0.05*x
l1=0.05*x
l2=1.5*l1
l3=0.5*l1
ang_P_Grados = 45 
ang_P_Rad=(45*np.pi)/180

P1=(l1*W)/2
P2=l2*W
P3=(l3*W)/2
Px=p*(sp.cos(ang_P_Rad))
Py = p*sp.sin(ang_P_Rad)
 
Ay=P1+P2+P3-Py
Ax=-Px
Ma=Ay*(l1+l2)-P1*(l2+(l1/3))-P2*(l2/2)+P3*(l3/3)-Py*l3 

# Tramo AB 0 < X <= l1

from sympy.abc import X
W_AB=(W*X)/l1 
V_AB=-(sp.integrate(W_AB,X))+Ay
M_AB=Ma+sp.integrate(V_AB,X)

V_ABev=V_AB.subs({X: l1})
M_ABev=M_AB.subs({X: l1})

# Tramo BC 0 < X <= l2

W_BC=W
V_BC=-(sp.integrate(W_BC,X))+V_ABev
M_BC=(sp.integrate(V_BC,X))+M_ABev

V_BCev=V_BC.subs({X: l2})
M_BCev=M_BC.subs({X: l2})

# Tramo CD 0 < X <= l3

W_CD=(-W*X)/l3
V_CD=-(sp.integrate(W_CD,X))+V_BCev
M_CD=(sp.integrate(V_CD,X))+M_BCev

V_CDev=V_CD.subs({X: l3})
M_CDev=M_CD.subs({X: l3})

#Cortante:
import matplotlib.pyplot as plt

def tramoAB(X):
    return(V_AB)
def tramoBC(X):
    return(V_BC)
def tramoCD(X):
    return(V_CD)
a=0
b=l1
c=l2
d=l3

X=np.linspace(a,d,1000)
y=np.piecewise(X,[(a<=X)&(X<b),(b<=X)&(X<c),(c<=X)&(X<=d)],[lambda X:tramoAB(X),lambda X:tramoBC(X),lambda X:tramoCD(X)])
tramoAB=np.vectorize(tramoAB)
plt.plot([X<b],tramoAB(X,[X<b]),label="Tramo AB")
plt.plot(X,([b<=X]&[X<c]),tramoBC(X,([b<=X]&[X<c])),label="Tramo BC")              
plt.plot(X,[(c<=x) & (X<=d)],tramoCD(X,[(c<=X) & (X<=d)]), label="Tramo CD")                

plt.grid(True)
plt.legend
hhh
                
                


    


