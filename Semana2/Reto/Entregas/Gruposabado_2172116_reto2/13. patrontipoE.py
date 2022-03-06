cantidad_pisos = 7

for i in range(7):
    if i == 0 or i == 6:
        print("*" * 5, end="")
    elif i == 1 or i ==2 or i == 4 or i == 5:
    else:
        print("*" * 4, end="")
    print()