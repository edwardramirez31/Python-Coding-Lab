#Crear un condicional para permitir que el usuario ingrese enteros o decimales sin producirse errores
Pregunta = input("¿Su número es entero o decimal?: ")
if Pregunta == "Entero" or Pregunta == "entero":
    
    #Pedir número al usuario
    A = input("ingrese número entero:")
    B = int(A)
elif Pregunta == "Decimal" or Pregunta == "decimal":
    A = input("ingrese número decimal:")
    B = float(A)

#Crear un contador con el fin de evitar que while sea infinito   
Contador = 0

#Determinar que la condición del contador sea menor a 10 ya que necesitamos la tabla del número de 1 a 10
while Contador < 10:
    X = B * (Contador + 1)
    Contador = Contador + 1
    print(f"{B} x {Contador} = {X}")