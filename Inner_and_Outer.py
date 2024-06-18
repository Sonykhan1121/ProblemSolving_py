import numpy as np
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = np.array(a)
b = np.array(b)
print(np.inner(a,b))
print(np.outer(a,b))