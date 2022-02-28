#Pedir un número y multiplicar ese número de 1 a 10
numero = int(input("Selecciona un numero "))

for i in range (1,11):
 print(f"{i}*{numero} = {i * numero}")
  #Es un bucle que se repite desde 1 hasta 10. Luego debemos imprimir la operación i*número hasta 10, y se ponen en corchetes...
  #...para que se tome el valor como variable, o, número.