import numpy as np
a=list(map(int, input().split()))

a = np.array(a)
a = np.reshape(a,(3,3))
print(a)