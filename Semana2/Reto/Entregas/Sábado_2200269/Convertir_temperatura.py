#Inputs: Valores de temperatura y unidades
Valor = float(input("VALOR TEMPERATURA:"))
Unidad = input("UNIDAD:")
#Realizar conversiones
Conversión_C_F = 9/5*Valor + 32
Conversión_F_C = 5/9*(Valor - 32)
#Output: Bucle para con condición para obtener la temperatura teniendo en cuenta la unidad inicial
for caracter in Unidad:
    if caracter == "C" or caracter == "c":
        print("TEMPERATURA EN F:",Conversión_C_F)

    elif caracter in Unidad == "F" or Unidad == "f":
        print("TEMPERATURA EN C:",Conversión_F_C)