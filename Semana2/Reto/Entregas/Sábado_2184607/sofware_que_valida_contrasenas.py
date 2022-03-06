import re
user_input = input("Ingrese contraseña\n")
pass_len = len(user_input)
if (pass_len < 6 or pass_len > 16):
    print('Contraseña Invalida')
    quit()

numeric = 0
upper_letters = 0
lower_letters = 0
especial_symbols = 0
for i in user_input:
    if i.isdigit():
        numeric += 1
    elif re.fullmatch(r'[A-Z]',i):
        upper_letters += 1
    elif re.fullmatch(r'[a-z]',i):
        lower_letters += 1
    elif re.fullmatch(r'[@#$]',i):
        especial_symbols += 1
    else:
        pass

print(numeric, upper_letters, lower_letters, especial_symbols)

if numeric and upper_letters and lower_letters and especial_symbols:
    print('Contraseña valida')
else:
    print('Contraseña Invalida')
