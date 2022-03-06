# validar contraseñas (los espacios tambien se consideran caracteres especiales)
contraseña = input("Ingrese su contraseña: ")
mayuscula = 0
minuscula = 0
numero = 0
especial = 0
longitud = 0
if len(contraseña)>=6 and len(contraseña)<=16:
        longitud += 1
for caracter in contraseña:
    if caracter.isalpha():
        if caracter.isupper():
              mayuscula += 1
        if caracter.islower():
             minuscula += 1
        else:
              especial += 1
    if caracter.isdigit():
          numero += 1
if mayuscula!=0 and minuscula!=0 and numero!=0 and especial!=0 and longitud!=0:
     print("Su contraseña es valida")
else:
    print("Su contraseña NO es valida, ingrese una que cumpla las condiciones indicadas.")
