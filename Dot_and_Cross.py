import numpy as np
n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
# print(*a)
# print(*b)
print(np.dot(a,b))
