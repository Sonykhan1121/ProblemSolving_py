import numpy as np
np.set_printoptions(legacy='1.13')
a = list(map(float,input().split()))
print(np.floor(np.array(a)))
print(np.ceil(np.array(a)))
print(np.rint(np.array(a)))

