import numpy as np
n , m = map(int,input().split())

a  = []
for i in range(n):
    a.append(list(map(int,input().split())))
a = np.array(a)
trns = a.flatten()
print(a.transpose())
print(trns)