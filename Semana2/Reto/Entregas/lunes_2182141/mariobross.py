print("ingrese las filas")
filas   = int(input ())
for i in range(filas) :
    print(' '*(filas-1-i) + '#'*(i+1) + ' ' + '#'*(i+1) )
    