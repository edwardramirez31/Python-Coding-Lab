print("ingrese las horas")
horas = int(input())
print("ingrese los minutos")
minutos = int(input())
print("ingrese los segundos")
segundos = int(input())

if horas==23 and minutos==59 and segundos==59 :
    print ("0h0m0s")
if  minutos==59 and segundos==59 :
    horas = horas + 1
    print (str(horas)+"h0m0s")
if  minutos !=59 and segundos ==59:
    minutos = minutos + 1
    print (str(horas)+"h"+str(minutos)+"m"+"0s")
if  segundos!=59:
    segundos = segundos + 1  
    print (str(horas)+"h"+str(minutos)+"m"+str(segundos)+"s")


