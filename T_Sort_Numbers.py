import copy
a = list(map(int,input().split()))
b = copy.copy(a)
a.sort()
for i in range(len(a)):
    print(a[i])
print()
for i in range(len(a)):
    print(b[i])