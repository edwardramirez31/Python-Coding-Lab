#Input: Insertar caracter para formar el patrón
P = " *"
#Código: utilizar el comando "for" y "range" para definir lo valores de las variables i, j y u
for i in range(1,4):
    N = i
    print(N*P)

for j in range(4,7):
    print(4*P)
# En el último tramo de "range" utilizo también "if", "elif" y else, ya que necesito posicionar el caracter de 3 maneras distintas.  
for u in range(7,10):
    if u == 7:
        print(3*P)
    elif u == 8:
        print(2*P)
    else:
        print(P)
