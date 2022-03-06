# Punto 1:

codigo=str(2162277)
x=0
for numero in codigo:
    sumar=int(numero)
    x+=sumar

import numpy as np
import sympy as sp
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

    # Datos:

y=x/3
W_max=0.005*x+0.01*(y) 
p=0.05*x
l1=0.05*x
l2=1.5*l1
l3=0.5*l1
L=(l1+l2+l3)
angulo_p_Grados=45 
angulo_p_Rad=(45*np.pi)/180

P1=(l1*W_max)/2
P2=l2*W_max
P3=(l3*W_max)/2
Px=p*(sp.cos(angulo_p_Rad))
Py=p*sp.sin(angulo_p_Rad)

    # Estatica:
 
Ay=P1+P2+P3-Py
Ax=-Px 
Ma=P1*(2*l1/3)+P2*((l2/2)+l1)+P3*((l3/3)+l1+l2)-Py*(l1+l2+l3) 

    # Fuerzas Internas:
    
    # TramoAB: 0<X<=l1
    
from sympy.abc import X
W_AB=(W_max*X)/l1 
V_AB=-(sp.integrate(W_AB,X))+Ay
M_AB=-Ma+sp.integrate(V_AB,X)

V_AB_Ev2=V_AB.subs({X: l1})
M_AB_Ev2=M_AB.subs({X: l1})

    # TramoBC: 0<X<=l2
    
W_BC=W_max
V_BC=-(sp.integrate(W_BC,X))+V_AB_Ev2
M_BC=(sp.integrate(V_BC,X))+M_AB_Ev2

V_BC_Ev2=V_BC.subs({X: l2})
M_BC_Ev2=M_BC.subs({X: l2})

    # TramoCD: 0<X<=l3
    
pend=W_max/(-l3)
W_CD=pend*X+W_max 
V_CD=-(sp.integrate(W_CD,X))+V_BC_Ev2 
M_CD=(sp.integrate(V_CD,X))+M_BC_Ev2

V_CD_Ev2=V_CD.subs({X: l3})
M_CD_Ev2=M_CD.subs({X: l3})

    # Grafica Cortante:

import matplotlib.pyplot as plt

X=np.arange(0,3.4,0.01)
tramo1=lambda X:-0.0833333333333333*X**2-0.271156654601839
tramo2=lambda X:-0.225*X-0.423031654601839
tramo3=lambda X:0.166666666666667*X**2-0.225*X-0.878656654601839

y=np.piecewise(X,[X<l1,(X>=0)&(X<=(l2)),X<=(l3)],[tramo1,tramo2,tramo3])
plt.plot(X,y)
plt.axhline(0)
plt.axvline(0)
plt.show()

    # Grafica Momento:

X=np.arange(0,(L+0.01),0.01)
tramo5=lambda X:-0.0277777777777778*X**3-0.271156654601839*X+2.37962976363745
tramo6=lambda X:-0.1125*X**2-0.423031654601839*X+1.94522452992497
tramo7=lambda X:0.0555555555555556*X**3-0.1125*X**2-0.878656654601839*X+0.627265116856242
y=np.piecewise(X,[X<l1,(X>=0)&(X<=(l2)),X<=(l3)],[tramo5,tramo6,tramo7])

plt.plot(X, y)
plt.axhline(0)
plt.axvline(0)
plt.show()


#Punto 2:

Mmax=np.amax(y)
Mmin=np.amin(y)

print("**********")
print("El momento maximo es: ",Mmax)

perfiles=pd.read_excel(r'C:\Users\MAFE\Desktop\ExcelTaller2.xlsx',usecols="A:D",index_col='Perfil')

h=perfiles.loc[1,'h[mm]']
b=perfiles.loc[1,'b[mm]']
e=perfiles.loc[1,'e[mm]']

Area=b*e+(h-e)*e

area1=e**2-e*h
area2=b*e
y1=(h-e)/2
y2=h-(e/2)
Eje_Neutro=(area1*y1+area2*y2)/(area1+area2)

inercia1=((e*(h-e)**3)/12)+area1*(Eje_Neutro-y1)**2
inercia2=((b*e**3)/12)+area2*(Eje_Neutro-y2)**2
InerciaZ=inercia1+inercia2

Esfuerzo=(Mmax*10**6*Eje_Neutro)/InerciaZ

Resultado=perfiles
    #Area Total:
Resultado['A[mm^2]']=perfiles['b[mm]']*perfiles['e[mm]']+(perfiles['h[mm]']-perfiles['e[mm]'])*perfiles['e[mm]']
    #Eje Neutro:
Resultado['EjeN[mm]']=((perfiles['e[mm]'])**2-(perfiles['e[mm]']*perfiles['h[mm]'])*((perfiles['h[mm]']-perfiles['e[mm]'])/2)+(perfiles['b[mm]']*perfiles['e[mm]'])*(perfiles['h[mm]']-(perfiles['e[mm]']/2)))/((perfiles['A[mm^2]']))
    #Inercia al rededor de Z:
Resultado['Iz[mm^4]']=((perfiles['e[mm]']/12)*(perfiles['h[mm]']-perfiles['e[mm]'])**3)+((perfiles['e[mm]'])**2-(perfiles['e[mm]']*perfiles['h[mm]']))*(perfiles['EjeN[mm]']-((perfiles['h[mm]']-perfiles['e[mm]'])/2))**2+((perfiles['b[mm]']/12)*(perfiles['e[mm]'])**3)+(perfiles['b[mm]']*perfiles['e[mm]'])*(perfiles['EjeN[mm]']-((perfiles['h[mm]'])-(perfiles['e[mm]']/2)))**2
    #Esfuerzo a Compresion: (Fibra superior)
Resultado['Esfuerzo_Comp[MPa]']=(Mmax*10**6*(perfiles['h[mm]']-perfiles['EjeN[mm]']))/perfiles['Iz[mm^4]']
    #Esfuerzo a Traccion: (Fibra inferior)
Resultado['Esfuerzo_Tens[MPa]']=(Mmax*10**6*(perfiles['EjeN[mm]']))/perfiles['Iz[mm^4]']
    #Perfiles con esfuerzo menor o igual al admisible:
filtro=Resultado['Esfuerzo_Tens[MPa]']<=250
    #Perfiles por area:
Resultado.loc[filtro,'A[mm^2]']
    #Perfil con menor area:
MenorArea=Resultado.loc[filtro, 'A[mm^2]'].min()
    #Posicion del perfil con menor area:
Posicion=Resultado.loc[filtro, 'A[mm^2]'].idxmin()
    #Perfil mas economico y cumple con el esfuerzo admisible:
PerfilEscogido=Resultado.loc[[Posicion], :'Esfuerzo_Tens[MPa]']

print("**********")
print("Tabla a exportar: ")
print(Resultado)

print("**********")
print("Perfil mas economico que cumple las condiciones de resistencia: ")
print(PerfilEscogido)







