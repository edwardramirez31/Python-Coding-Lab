numero_ingresado=int(input())
residuo= numero_ingresado% 2 
if numero_ingresado < 0 and residuo == 0:
    print("su numero es par y es negativo")
elif residuo == 0:
    print("su numero es par")    
else: 
     print("su numero es impar")   
   
