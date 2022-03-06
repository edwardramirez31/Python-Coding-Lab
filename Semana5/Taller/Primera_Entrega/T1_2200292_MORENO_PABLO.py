import numpy as np 
E = 200 * 1000
l = 3.4
l1 = 1.5
x = 17
fs_flu = float(1.17)
esf_adm_flu_ten = 250 / fs_flu
esf_adm_flu_cor = 145 / fs_flu
#CABLE BC BD BE Se analizará entonces el esfuerzo normal para saber la fuerza máxima que pueden resistir
area_cables = np.pi * ((1/4)/2 * 25.4)**2 
area_pernos = np.pi * ((1/2)/2 * 25.4)**2     
fuerza_cables = area_cables * esf_adm_flu_ten      
#PERNOS CORTANTE SIMPLE C D E Se analizará el esfuerzo cortante para saber la fuerza máxima que pueden resistir
fuerza_pernos_simples = area_pernos * esf_adm_flu_cor
#PERNOS CORTANTE DOBLE A B Se analizará el esfuerzo cortante para saber la fuerza máxima que pueden resistir
fuerza_pernos_doble = 2 * area_pernos * esf_adm_flu_ten 
# Comparando estos valores de fuerzas anteriores en cada elemento, debemos encontrar la menor que será la que fallará primero y tomaremos esa para hallar el resto de incognitas
fuerza_max = min(fuerza_cables,fuerza_pernos_simples,fuerza_pernos_doble)


#HALLAREMOS EL VALOR DE WMAX MEDIANTE LA ESTÁTICA TENIENDO EN CUENTA LA FUERZA MÁXIMA QUE PUEDEN SOPORTAR LOS CABLES
angulo_BC = 40 
angulo_BE = 50 

#SUMATORIA DE FUERZA EN X
#Ax - np.sin(angulo_BC)*fuerza_max + np.sin(angulo_BE)*fuerza_max = 0
#SUMATORIA DE FUERZA EN Y
#Ay - WMAX + np.cos(angulo_BC)*fuerza_max + np.cos(angulo_BE)*fuerza_max + fuerza_max = 0
#SUMATORIA DE MOMENTOS EN A
#l * np.cos(angulo_BC)*fuerza_max + l * np.cos(angulo_BE)*fuerza_max + l * fuerza_max - l/2 * WMAX = 0 

#Ax,AY,WMAX,
matriz = np.array([
    [1, 0, 0], 
    [0, 1, -1],
    [0, 0, - l/2 ]
])
vector = np.array([np.sin(angulo_BC)*fuerza_max-np.sin(angulo_BE)*fuerza_max, -np.cos(angulo_BC)*fuerza_max - np.cos(angulo_BE)*fuerza_max - fuerza_max, -l * np.cos(angulo_BC)*fuerza_max - l * np.cos(angulo_BE)*fuerza_max - l * fuerza_max])
solucion = np.linalg.solve(matriz,vector)
WMAX = solucion[2]

#SE CALCULARAN LAS DEFORMACIONES EN LOS CABLES 
#CABLE BC
defor_cable_BC = fuerza_max * l1 / (area_cables * E )
#CABLE BD
defor_cable_BD = fuerza_max * l1 / (area_cables * E )
#CABLE BE
defor_cable_BE = fuerza_max * l1 / (area_cables * E )

#RESULTADOS 
# FUERZAS
AX = solucion[0]
AY = solucion[1]
WMAX = solucion[2]
CABLE_CB = fuerza_max
CABLE_CD = fuerza_max
CABLE_CE = fuerza_max

float(fuerza_max)
float(defor_cable_BC)

lista1 = ["CABLE_CB", "CABLE_CD", "CABLE_CE"]


for i in lista1:
    print("La fuerza a tensión del " + str(i) + " es igual a " + str(fuerza_max) + " Newtons")

for i in lista1:
    print("La deformación del " + str(i) + " es igual a " + str(defor_cable_BC) + " milimetros al cuadrado")

print("La fuerza en la reacción AX es igual a " + str( solucion[0]) + " Newtons")
print("La fuerza en la reacción AY es igual a " + str( solucion[1]) + " Newtons")
print("La fuerza máxima que puede tomar la fuerza W es igual a " + str( solucion[2]) + " Newtons")
  

   