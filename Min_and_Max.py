import numpy as np
n ,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
print(max(np.min(a,axis = 1)))