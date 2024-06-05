import itertools
n ,  m = map(int,input().split())
a = []
for i in range(n):
    now = list(map(int,input().split()))
    a.append(now[1:])
# print(a)
result =0
for i in itertools.product(*a):
    total =0
    for j in i:
        total+=((j*j)%m)
    result = max(total%m,result)
print(result)

