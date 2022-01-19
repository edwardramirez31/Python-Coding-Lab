password = input("enter your password")

if len(password) < 6 or len(password) > 16:
    print("contraseña incorrecta")
else:
        tiene_misnuculas = False
        tiene_mayuscula = False
        tiene_numeros = False
        tiene_caracter_especial = False

        for caracter in password:
            if caracter.isalpha() and caracter.islower():
                tiene_minusculas = True
            elif caracter.isalpha() and caracter.isupper():
                tiene_mayusculas = True
            elif caracter.isdigit():
                tiene_numeros = True
            elif caracter == "#" or caracter == "$" or caracter == "@":
                tiene_caracter_especial = True

        if tiene_minusculas and tiene_mayusculas and tiene_caracter_especial and tiene_numeros:
            print("constraseña valida")
        else:
            print("la constraseña es invalida")