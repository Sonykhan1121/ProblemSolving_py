import numpy as np

a = list(map(float,input().split()))
x = int(input())
f = np.poly1d(a)
print(f(x))

