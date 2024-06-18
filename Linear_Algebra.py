import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(list(map(float,input().split())))

ans = np.linalg.det(a)
print(round(ans,2))