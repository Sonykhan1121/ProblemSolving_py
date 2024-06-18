import numpy

n , m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
# print(a)
print(numpy.mean(a,axis = 1))
print(numpy.var(a,axis = 0))
print(round(numpy.std(a,axis =None),11))