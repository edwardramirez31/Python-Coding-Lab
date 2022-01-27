#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

carga_inicial = 20
factor_suma_carga = 0.25
carga_final = carga_inicial + (18 * factor_suma_carga)

distancia_AD = 1
distancia_AB = 2
distancia_BC = 2
distancia_BE = 1
distancia_AC = 4

angulo_barra_EC = np.arctan(distancia_AD / distancia_BC)
angulo_barra_AE = np.arctan(distancia_AD / distancia_AB)


# In[2]:


rango_cargas = np.arange(carga_inicial, carga_final, factor_suma_carga )
rango_angulos = np.arange(0, 180, 10)


# In[ ]:


def calcular_reacciones(carga, angulo, distancia_AC):
    angulos_radianes = angulo * np.pi / 180
    Ay = carga * np.cos(angulos_radianes)
    Dx = distancia_AC * carga * np. sin(angulos_radianes)
    Ax = carga * np.sin(angulos_radianes) - Dx
    return Ax, Ay, Dx


# In[ ]:



def calcular_fuerzas_nodo_C(carga, angulo, angulo_barra_EC):
    angulos_radianes = angulo * np.pi / 180
    CE = carga * np. cos(angulos_radianes) /  np. sin(angulo_barra_EC)
    BC = carga * np. sin(angulos_radianes) - CE *  np. cos(angulo_barra_EC)
    return CE, BC


def calcular_fuerzas_nodo_B(fuerza_BC):
    BA = fuerza_BC
    BE = 0
    return BA, BE 


def calcular_fuerzas_nodo_E(CE, angulo_barra_AE, angulo_barra_EC):
    EA = - CE * np.sin(angulo_barra_EC) / np.sin(angulo_barra_AE)
    ED = - EA * np.cos(angulo_barra_AE) + CE * np.cos(angulo_barra_EC)
    return EA, ED


def calcular_fuerzas_nodo_D(Dx):
    ED = - Dx
    DA = 0
    return ED, DA


def calcular_fuerzas_nodo_A(Ax, Ay, angulo_barra_AE,):
    AE = Ay / np.sin(angulo_barra_AE)
    AB = - Ax - AE * np.cos(angulo_barra_AE)
    return AE, AB


# In[ ]:


fuerza_maxima = np.array([0, 0, 0, 0, 0, 0, 0])
for angulo, carga in zip(rango_angulos, rango_cargas):
    Ax, Ay, Dx = calcular_reacciones(carga, angulo, distancia_AC)
    CE, BC = calcular_fuerzas_nodo_C(carga, angulo, angulo_barra_EC)
    BA, BE = calcular_fuerzas_nodo_B(BC)
    EA, ED = calcular_fuerzas_nodo_E(CE, angulo_barra_AE, angulo_barra_EC)
    DE, DA = calcular_fuerzas_nodo_D(Dx)
    AE, AB = calcular_fuerzas_nodo_A(Ax, Ay, angulo_barra_AE,)
    print(f"Reacciones angulo {angulo} grados: ")
    print(Ax, Ay, Dx)
    print("Fuerzas internas:")
    print(BA, EA, DA, BC, BE, CE, ED)
    print(f"{AE} == {EA}, {AB} == {BA}, {DE} == {ED}")
    print()
    fuerza_maxima[0] = BA if np.absolute(BA) > fuerza_maxima[0] else fuerza_maxima[0]
    fuerza_maxima[1] = BC if np.absolute(BC) > fuerza_maxima[1] else fuerza_maxima[1]
    fuerza_maxima[2] = CE if np.absolute(CE) > fuerza_maxima[2] else fuerza_maxima[2]
    fuerza_maxima[3] = ED if np.absolute(ED) > fuerza_maxima[3] else fuerza_maxima[3]
    fuerza_maxima[4] = EA if np.absolute(EA) > fuerza_maxima[4] else fuerza_maxima[4]
    fuerza_maxima[5] = DA if np.absolute(DA) > fuerza_maxima[5] else fuerza_maxima[5]
    fuerza_maxima[6] = BE if np.absolute(BE) > fuerza_maxima[6] else fuerza_maxima[6]
        
print(fuerza_maxima)


# In[ ]:


esfuerzo_admisible = 15
area = 300


# In[ ]:


fuerza_maxima = esfuerzo_admisible * area /1000


# In[ ]:


fuerzas_internas = np.array([0, 0, 0, 0, 0, 0, 0])
for angulo, carga in zip(rango_angulos, rango_cargas):
     Ax, Ay, Dx = calcular_reacciones(carga, angulo, distancia_AC)
     CE, BC = calcular_fuerzas_nodo_C(carga, angulo, angulo_barra_EC)
     BA, BE = calcular_fuerzas_nodo_B(BC)
     EA, ED = calcular_fuerzas_nodo_E(CE, angulo_barra_AE, angulo_barra_EC)
     DE, DA = calcular_fuerzas_nodo_D(Dx)
     AE, AB = calcular_fuerzas_nodo_A(Ax, Ay, angulo_barra_AE,)
     fuerzas_internas = np.array([("AB", BA), ("AE", EA), ("AD", DA), ("BC", BC), ("BE", BE), ("CE", CE), ("ED", ED)])
     elementos_que_fallan = np.where(np.absolute(np.array([x[1] for x in fuerzas_internas], dtype=np.float64)) > fuerza_maxima)
     if len(elementos_que_fallan) > 0:
        print(f"La primera falla se presenta bajo la carga de {carga} kN y la direccion de {angulo} grados ")
        for i in elementos_que_fallan[0]:
            fuerza = fuerzas_internas[i][1].astype(float)
            causa_falla = "compresión" if fuerza < 0 else "tracción"
            print(f"El elemento {fuerzas_internas[i][0]} falla bajo la carga {np.absolute(fuerza)} kN a {causa_falla}")
        print()


# In[ ]:


L = 3
aumento_distancia = float("0.0" + str(L))
A = 0
B = 7

AB = 7
AB = round(AB / 10) * 10

distancia_AC = 2
distancia_AB = 2


# In[ ]:


for angulo, carga in zip(rango_angulos, rango_cargas):
    distancia_AC += aumento_distancia
    distancia_AB += aumento_distancia
    angulo_barra_inclinada_AE = np.arctan(distancia_AD / distancia_AB)
    Ax, Ay, Dx = calcular_reacciones(carga, angulo, distancia_AC)
    CE, BC = calcular_fuerzas_nodo_C(carga, angulo, angulo_barra_EC)
    BA, BE = calcular_fuerzas_nodo_B(BC)
    EA, ED = calcular_fuerzas_nodo_E(CE, angulo_barra_AE, angulo_barra_EC)
    DE, DA = calcular_fuerzas_nodo_D(Dx)
    AE, AB = calcular_fuerzas_nodo_A(Ax, Ay, angulo_barra_AE,)
    fuerzas_internas = [("AB", BA, carga), ("AE", EA, carga), ("AD", DA, carga), ("BC", BC, carga), ("BE", BE, carga), ("CE", CE, carga), ("ED", ED, carga)]
    print(f"Para un aumento de distancia de {distancia_AB - 2} las fuerzas calculadas son:")
    print(fuerzas_internas)
    print()


# In[ ]:




