n = int(input())
a = list(map(int,input().split()))

min = 1000000
min_index = -1
max = -1000000
max_index = -1

for i in range(n):
    if(a[i]<min):
        min = a[i]
        min_index = i
    if(a[i]>max):
        max = a[i]
        max_index = i

a[min_index],a[max_index] = max,min

for i in range(n):
    print(a[i],end=' ')