Lista = [0,1,2,3,4,5,6]
l = []
for i in Lista:
    if i != 3 and i != 6:
        omitidos = i
        l.append(omitidos)
print(l)