import numpy as np

a = np.array([1, 2, 3])

parte1 = np.repeat(a, 3)
parte2 = np.tile(a, 3)
print(np.hstack((parte1,parte2)))