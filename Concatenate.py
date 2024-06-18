import numpy as np
n , m , p = map(int ,input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(m):
    b.append(list(map(int,input().split())))

ans = np.concatenate((a,b),axis =0)
print(ans)