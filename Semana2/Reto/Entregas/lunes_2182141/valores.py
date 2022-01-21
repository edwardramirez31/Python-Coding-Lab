nb1 = int(input("Enter nb1:"))
nb2 = int(input("Enter nb2:"))
nb3 = int(input("Enter nb3:"))

if nb1 > nb2:
    nb1 = nb3 * 2
else:
    nb1 = nb1 + 1
    if nb2 > nb3:
        nb1 = nb1 + nb3 * 3
    else:
        nb1 = 0
        nb3 = nb3 * 2 + nb2

print(nb1, nb2, nb3)
