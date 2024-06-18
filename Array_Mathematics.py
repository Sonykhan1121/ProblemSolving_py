import numpy as np
n , m  = map(int,input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))

a = np.array(a)
b = np.array(b)
result = []
result.append(a+b)
result.append(a-b)
result.append(a*b)
result.append(a//b)
result.append(a%b)
result.append(a**b)
for i in result:
    print(np.array(i,ndmin=2))
