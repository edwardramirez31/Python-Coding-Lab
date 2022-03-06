import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print (arr)
filtro = arr[arr%2 != 0]
print(filtro)

