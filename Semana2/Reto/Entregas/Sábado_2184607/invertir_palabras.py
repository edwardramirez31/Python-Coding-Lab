user_input = input("Ingresa una palabra")
inverted = ""
for index in range(len(user_input)-1,-1,-1):
    inverted += user_input[index]
print(inverted)