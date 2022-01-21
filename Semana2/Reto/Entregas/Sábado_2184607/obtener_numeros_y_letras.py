user_input = input()
letters = 0  # initiating the count of letters to 0
numeric = 0  # initiating the count of numbers to 0

for i in user_input:
    if i.isdigit():
        numeric += 1
    elif i.isalpha():
        letters += 1
    else:
        pass

print ("Las letras ingresadas fueron ", letters, "y los digitos ", numeric)
