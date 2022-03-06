import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a)
print(b)
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))