import numpy as np
a = np.array([1,2,3])
print(np.full((1,3),a[0]))
print(np.concatenate(( np.full((1,3),a[0])  , np.full((1,3),a[1])  , np.full((1,3),a[2]) ,a,a,a,),axis=None))