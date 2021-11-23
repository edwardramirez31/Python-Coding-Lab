# PROBLEMA: Quiero un software que calcule el promedio de mis notas del semestre (n cantidad de notas)
# INPUT: Las notas, n cantidad de notas
# 1. Pedir n cantidad de notas
cantidad_de_notas = int(input())

if cantidad_de_notas <= 0:
    print("Ingrese una cantidad valida")
else:
    # 2. Pedir la nota de cada materia
    """
    inicializo contador 1 con el fin de actualizarlo con respecto al tiempo y que el bucle se ejecute mientras el contador sea menor o igual a la cantidad de notas ingresadas
    """
    contador = 1
    """
    inicializo suma como 0 para ir sobre escribiendo esta variable, sumando las notas que ingresa el usuario
    """
    suma = 0

    # si el contador es menor o igual a la cantidad de notas, ejecutar el código y volver a evaluar la condicion
    while contador <= cantidad_de_notas:
        print("Cual es la nota de tu materia " + str(contador))
        nota_ingresada_por_usuario = int(input())
        suma = suma + nota_ingresada_por_usuario
        # sobre escribo contador para saber mi iteracion actual
        contador = contador + 1

    # 3. Calcular el promedio = suma de todos mis numeros / cantidad
    print("Su promedio es " + str(suma / cantidad_de_notas))
# OUTPUT: Promedio final
