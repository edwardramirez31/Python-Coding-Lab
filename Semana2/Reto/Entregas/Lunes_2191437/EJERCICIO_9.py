# EJERCICIO 9
# Fizzbuzz

# 1. Definir la lista de numeros
for i in range (1, 50):
    
    # 2. Definir la condicion
    if i % 3 == 0:
        
        # 3. Mostrar la salida segun las condiciones
        print ("Fizz")

    if i % 5 == 0:
        print ("Buzz") 
    
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    
    print (i)
    