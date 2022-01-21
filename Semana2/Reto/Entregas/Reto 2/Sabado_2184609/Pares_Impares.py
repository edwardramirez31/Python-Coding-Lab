user_input = input("Ingresa secuencia")
odd = 0
even = 0

num_list = []

for number in user_input.split(", "):
    num_list.append(int(number))

for number in num_list:
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Pares ", even)
print("Impares ", odd)