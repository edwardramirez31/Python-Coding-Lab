cantidad_pisos = 4

for i in range(cantidad_pisos):
    print(" " * (cantidad_pisos - (i + 1)) + "#" * (i + 1), end="")
    print("  " + "#" * (i + 1))