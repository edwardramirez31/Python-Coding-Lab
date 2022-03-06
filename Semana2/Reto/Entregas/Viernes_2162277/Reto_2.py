
#Iterar y usar condiciones
for i in range(1499,2701):
    cond1=i%5==0
    cond2=i%7==0    
    if(cond1 and cond2):
        print(i)
print("---Fin del programa---")


#Convertir temperatura
temp=input("Por favor ingrese la temperatura actual: ")
while not(temp.endswith("C") or temp.endswith("F")):
    temp=input("Por favor ingrese un dato correcto: ")
if(temp.endswith("C")):
    enterotemp=int(temp[:-1])
    salidaF=(enterotemp*1.8)+32
    print("La temperatura en °F es:",salidaF,"°F")
    print("Gracias")
elif(temp.endswith("F")):
    enterotemp=int(temp[:-1])
    salidaC=(enterotemp-32)/1.8
    print("La temperatura en °C es:",salidaC,"°C")
    print("---Gracias---")
    

#Adivina el numero
print("---Adivine el numero de 1 a 9---")
n=int(input("Por favor diga su prediccion: "))
import random as rd
numeroazar=rd.randint(1,9)
print("El numero es:",numeroazar)
while not (n==numeroazar):
    print("Mala suerte")
    n=int(input("Ingrese un nuevo numero: "))
    numeroazar=rd.randint(1,9)
    print("El numero es:",numeroazar)
print("¡Muy Bien!")
print("---Programa terminado---") 


#Patron de caracteres
n=4
for i in range(1,n+1):
    for j in range(i):
        print('* ', end='')
    print()  
print("* * * *")
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end='')
    print()  


#Invertir palabras con un bucle
cadena=input("Por favor ingrese una palabra: ")
invertida=cadena[::-1]
print("Su palabra invertida es:",invertida)
print("---Gracias---")    
  
  
#Pares e impares
n=int(input("Digite por favor la cantidad de numeros que va a ingresar: "))
cuentaP=0
cuentaI=0
ciclos=0
while(ciclos<n):
    m=int(input("Digite un numero: "))
    ciclos+=1
    cond1=m%2==0
    if cond1:
        cuentaP+=1
    else:
        cuentaI+=1
print("La cantidad de pares es:",cuentaP)
print("La cantidad de impares es:",cuentaI)
print("---Fin del programa---")
   
   
#Omitir valores
for i in range(0,7):
    if not(i==3 or i==6):
        print(i)    
    

#Serie de Fibonacci 
print("----Serie Fibonacci---")
n=int(input("Hasta que posicion desea que avance la serie? "))
m=n//2
n1=0
n2=1
if (n%2==0):
    for i in range(0,m):
        print(n1," ",n2, end="   ")
        n1=n1+n2
        n2=n1+n2
else:
    for i in range(0,m):
        print(n1," ",n2, end="   ")
        n1=n1+n2
        n2=n1+n2
    print(n1)
print("---Gracias---")


#Hagamos Fizz Buzz
print("---FizzBuzz---")
for i in range(0,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
print("---Gracias---")


#Contando numeros binarios
entrada=(input("Ingrese la secuencia de numeros binarios separados por una coma: "))
lista=(entrada.split(','))
salida=[]
for binario in lista:
    binarioinv=binario[::-1]
    ciclo=0
    dec=0
    for digito in binarioinv:
        predec=int(digito)*2**ciclo
        ciclo+=1
        int(predec)
        dec+=predec
    if(dec%5==0):
        salida.append(binario)
sal1=(str(salida).replace("[","").replace("'","").replace("]",""))
print("Los numeros binarios divisibles en 5 son: ",sal1)
print("---Gracias---")


#Obtener numeros y letras
from typing import final
cadena=input("Por favor digite su cadena alfanumerica: ")
cuentaL=0
cuentaN=0
cuentaE=0
for caracter in cadena:
    if(caracter.isdigit()):
        cuentaN+=1
    elif(caracter.isalpha()):
        cuentaL+=1
    else:
        cuentaE+=1        
print("La cantidad de letras en su cadena es:",cuentaL)
print("La cantidad de numeros en su cadena es:",cuentaN)
print("La cantidad de caracteres NO alfanumericos en su cadena es:",cuentaE)
print("---Gracias---")


#Patrones
print("----E----")
cadena=[5,1,1,4,1,1,5]
n=""
for member in cadena:
    n=str(member*"*")
    print(n)
    
print("---Mario Bros---")
n=int(input("Ingrese la cantidad de filas que desea: "))
for i in range(1,n+1):
    patron=i*"#"+" "+i*"#"
    print("{:^20}".format(patron)) 


#Tablas de multiplicar
n=int(input("Por favor digite un numero: "))
print("---La tabla de multiplicar del",n,"es:---")
for i in range(0,11):
    mult=(i*n)
    print(i,"X",n,"=",mult)
print("---Gracias---")


#Obtener el siguiente segundo
tiempo=input("Por favor ingrese las horas, los minutos y los segundos separados por una coma: ")
listaT=(tiempo.split(","))
hrs=int((listaT[0]))
mins=int((listaT[1]))
segs=int((listaT[2]))
while (hrs>=24 or mins>=60 or segs>=60):
    tiempo=input("Por favor ingrese el tiempo en el formato correcto: ")
    listaT=(tiempo.split(","))
    hrs=int((listaT[0]))
    mins=int((listaT[1]))
    segs=int((listaT[2]))
segs+=1
if(segs==60):
    segs="00"
    mins+=1
    if(mins==60):
        mins="00"
        hrs+=1
        if(hrs==24):
            hrs="00"
print("El tiempo en el siguiente segundo es:",hrs,"horas",mins,"mins",segs,"segundos")
print("---Gracias---")


#Validador de contraseñas (Pend)
print("Su contraseña debe tener al menos:") 
print("-.Un caracter (a,z) y un caracter (A,Z)")
print("-.Un caracter numerico (a,z)")
print("-.Un caracter NO alfa-numerico (#,%,&)")
print("-.Un minimo de 6 y maximo de 16 caracteres")
contra=input("Por favor ingrese su contraseña: ")
for caracter in contra:
    if(caracter.isdigit):
        print("mal")


  