fibonacci = [0, 1]

for number in range(1,51):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(fibonacci)