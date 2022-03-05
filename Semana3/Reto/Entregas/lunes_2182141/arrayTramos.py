import numpy as np
x = np.arange(0,501,10)
print(x)

x_1 = x[x <= 100]
print(x_1)
y_1 = 1 / 3 * (x_1 ** 2) - 20
print(y_1)

x_2 = x[(x >= 100) & (x <= 350)]
print(x_2)
y_2 = - 1 / 3* x_2 + 5
print(y_2)

x_3 = x[(x >= 350) & (x <= 500)]
print(x_3)
y_3 = - 5 * x_3 + 2
print(y_3)

