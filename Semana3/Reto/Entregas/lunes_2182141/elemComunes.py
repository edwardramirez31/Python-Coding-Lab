import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a,b)
print(c)

print(np.concatenate((   np.where(a == 2)  ,   np.where(a == 4)    ),axis=1))
