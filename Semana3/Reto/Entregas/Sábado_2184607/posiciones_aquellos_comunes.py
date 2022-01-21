import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array ([7,2,10,2,7,4,9,4,9,8])
arr1 = np.in1d(a,b)
result = np.where(arr1 == True)
print(result[0])