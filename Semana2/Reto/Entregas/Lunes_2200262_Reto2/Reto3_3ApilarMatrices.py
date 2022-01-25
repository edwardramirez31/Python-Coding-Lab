import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)

#vstack nos permite apilar directamente 2 matrices de forma vertical.
np.vstack([a,b])

