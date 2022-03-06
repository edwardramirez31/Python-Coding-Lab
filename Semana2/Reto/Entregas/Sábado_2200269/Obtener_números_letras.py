#Crear una función que cuente los digitos y las letras de una cadena de caracteres
def contar_digitos_letras(cadena):
    
    #Denifir el contador para letras y digitos, empezando en cero
    Letras = 0
    Digitos = 0

    #Desarrollar un bucle que pase por todos los componentes de la cadena
    for i in cadena:
        
        #utilizar la función variable.isalpha() para saber si es una letra
        if i.isalpha():
            Letras = Letras + 1
        
        #Utilizar la función variable.isdigit() para saber si es un digito
        elif i.isdigit():
            Digitos = Digitos + 1
    
    #Definir lo que me devolverá la función con la palabra return
    return f"las letras ingresadas fueron {Letras} y los digitos {Digitos}"

#Uilizar la función input para permitir que el usuario ingrese la palabra que desee
Palabra = input("INGRESE CADENA DE TEXTO:")

#Utilizar la fúnción creada e imprimir el resultado obtenido
Resultado = contar_digitos_letras(Palabra)
print (Resultado)