from traceback import print_tb
import numpy as np

carga_inicial = 20
diferencial_carga = 0.25
carga_final = carga_inicial + 18 * diferencial_carga

distancia_AD = 1
distancia_AB = 2
distancia_BC = 2
distancia_AC = distancia_AB+ distancia_BC

ángulo_barra_inclinada = np.arctan(distancia_AD / distancia_BC)
ángulo_barra_inclinada_AE = np.arctan(distancia_AD / distancia_AB)

rango_de_ángulos = np.arange(0, 190, 10)
rango_de_cargas = np.arange(carga_inicial, carga_final + diferencial_carga, diferencial_carga)
rango_de_cargas
print(rango_de_cargas)

def cálculo_reacciones(carga, ángulo, distacia_AC):
    ángulo_radianes = (ángulo if ángulo <= 90 else 180 - ángulo) * np.pi / 180
    Ay = (-1 if ángulo <= 90 else 1) * carga * np.cos(ángulo_radianes)
    Dx = (-1 if ángulo <= 90 else 1) * distancia_AC * carga * np.cos(ángulo_radianes)
    Ax = - Dx - carga * np.sin(ángulo_radianes)
    return Ax, Ay, Dx

def  cálculo_fuerzas_nodo_C(carga, ángulo):
    ángulo_radianes =(ángulo if ángulo <= 90 else 180 - ángulo) * np.pi / 180
    CE = (1 if ángulo <= 90 else -1) * carga * np.cos(ángulo_radianes) / np.sin(ángulo_barra_inclinada)
    BC = carga * np.sin(ángulo_radianes) - CE * np.cos(ángulo_barra_inclinada)
    return CE, BC

def cálculo_fuerzas_nodo_B(fuerza_BC):
    BA = fuerza_BC
    BE = 0
    return BA, BE

def cálculo_fuerzas_nodo_E(fuerza_CE, ángulo_barra_inclinada_AE):
    EA = fuerza_CE * np.sin(ángulo_barra_inclinada) / np.sin(ángulo_barra_inclinada_AE)
    ED = EA * np.cos(ángulo_barra_inclinada_AE) + fuerza_CE * np.cos(ángulo_barra_inclinada)
    return EA, ED

def cálculo_fuerzas_nodo_D(fuerza_Dx):
    ED = - fuerza_Dx
    DA = 0
    return ED, DA

def cálculo_fuerzas_nodo_A(Ax, Ay, ángulo_barra_inclinada_AE):
    AE = Ay / np.sin(ángulo_barra_inclinada_AE)
    AB = Ax / np.cos(ángulo_barra_inclinada_AE)
    return AE, AB

fuerza_maxima = np.array([0, 0, 0, 0, 0, 0, 0])
for ángulo, carga in zip(rango_de_ángulos, rango_de_cargas):
    Ax, Ay, Dx = cálculo_reacciones(carga, ángulo, distancia_AC)
    CE, BC = cálculo_fuerzas_nodo_C(carga, ángulo)
    BA, BE = cálculo_fuerzas_nodo_B(BC)
    EA, ED = cálculo_fuerzas_nodo_E(CE, ángulo_barra_inclinada_AE)
    DE, DA = cálculo_fuerzas_nodo_D(Dx)
    AE, AB = cálculo_fuerzas_nodo_A(Ax, Ay, ángulo_barra_inclinada_AE)
    print(f"Reacciones ángulo", ángulo, "grados: ")
    print(Ax, Ay, Dx)
    print("Fuerzas internas: BA, EA, DA, BC, BE, CE, ED")
    print(BA, EA, DA, BC, BE, CE, ED)
    print("AE == EA,  AB == BA,  DE == ED")
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

######
## Esfuerzo admisible en MPa
esfuerzo_admisible = 21
## Área de la sección en mm2
área = 1200
## Fuerza máxima en KN
fuerza_maxima = esfuerzo_admisible * área / 1000
fuerza_maxima
print("Fuerza máxima = ", fuerza_maxima)

fuerzas_internas = np.array([0, 0, 0, 0, 0, 0, 0])
for ángulo, carga in zip(rango_de_ángulos, rango_de_cargas):
    Ax, Ay, Dx = cálculo_reacciones(carga, ángulo, distancia_AC)
    CE, BC = cálculo_fuerzas_nodo_C(carga, ángulo)
    BA, BE = cálculo_fuerzas_nodo_B(BC)
    EA, ED = cálculo_fuerzas_nodo_E(CE, ángulo_barra_inclinada_AE)
    DE, DA = cálculo_fuerzas_nodo_D(Dx)
    AE, AB = cálculo_fuerzas_nodo_A(Ax, Ay, ángulo_barra_inclinada_AE)
    fuerzas_internas = np.array([("AB", BA), ("AE", EA), ("AD", DA), ("BC", BC), ("BE", BE), ("CE", CE), ("ED", ED)])
    elemento_falla = np.where(np.absolute(np.array([x[1] for x in fuerzas_internas], dtype=np.float64)) > fuerza_maxima)
    if len(elemento_falla) > 0:
        print(f"la primera falla se presenta en la carga de: ", carga, "KN en la dirección de ", ángulo, "grados")
        for i in elemento_falla[0]:
            fuerza = fuerzas_internas[i][1].astype(float)
            causa_falla = "compresión" if fuerza < 0 else "tracción"
            print(f"El elemento {fuerzas_internas[i][0]} falla bajo la carga {np.absolute(fuerza)} KN a {causa_falla}")
        print()

#### TERCER PUNTO
## Código 2194034, valor de L tomado es el 4, por que el quinto número es 0
L = 4
aumento_distancia = float("0.0" + str(L))
A = 3
B = 4
AB = 50
AB = round(AB / 10) * 10
AB, aumento_distancia
print("Ángulo AB:",AB,",","Aumento de distancia de:" ,aumento_distancia)

for ángulo, carga in zip(rango_de_ángulos, rango_de_cargas):
    distancia_AC += aumento_distancia
    distancia_AB += aumento_distancia
    ángulo_barra_inclinada_AE = np.arctan(distancia_AD / distancia_AB)
    Ax, Ay, Dx = cálculo_reacciones(carga, ángulo, distancia_AC)
    CE, BC = cálculo_fuerzas_nodo_C(carga, ángulo)
    BA, BE = cálculo_fuerzas_nodo_B(BC)
    EA, ED = cálculo_fuerzas_nodo_E(CE, ángulo_barra_inclinada_AE)
    DE, DA = cálculo_fuerzas_nodo_D(Dx)
    AE, AB = cálculo_fuerzas_nodo_A(Ax, Ay, ángulo_barra_inclinada_AE)
    fuerzas_internas = [("AB", BA, carga), ("AE", EA, carga), ("AD", DA, carga), ("BC", BC, carga), ("BE", BE, carga), ("CE", CE, carga), ("ED", ED, carga)]
    print(f"Aumento de distancia de:", distancia_AB - 2, "Las fuerzas calculadas son:")
    print(fuerzas_internas)
    print()