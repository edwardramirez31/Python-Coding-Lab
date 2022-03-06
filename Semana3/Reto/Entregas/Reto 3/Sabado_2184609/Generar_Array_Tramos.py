import numpy as np

def funcion_a(x):
    return 1 / 3 * (x ** 2) - 20

def funcion_b(x):
    return -1 / 3 * x + 5

def funcion_c(x):
    return -5 * x + 2

x = np.arange(0,500,1)

r = np.piecewise(x, [x <= 100, (x > 100) & (x <= 350), (x > 350) & (x <= 500)], [lambda x: funcion_a(x), lambda x: funcion_b(x), lambda x: funcion_c(x)])
print(r)