import numpy as np
arr = np.arange(1,31)
matriz = arr.reshape((6,5))
print(matriz)
silicing1 = matriz[2:4 , :2 ]
print(silicing1)

silicing2 = matriz[ [0,4,5]   ,  3:  ]
print(silicing2)

silicing3 = matriz[ [0,1,2,3]   ,  [1,2,3,4]  ]
print(silicing3)