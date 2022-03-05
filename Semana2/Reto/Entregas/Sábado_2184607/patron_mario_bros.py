user_input = int(input("Ingresa numero de filas"))
for index in range(1, user_input + 1):
    spaces = user_input - index
    print(" " * spaces, "#" * index, "#" * index)
