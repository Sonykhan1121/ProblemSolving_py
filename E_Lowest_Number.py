n = int(input())
a = list(map(int,input().split()))
min = 100000
index  = 1;
for i in range(n):
    if a[i] < min:
        min = a[i]
        index = i+1
print(min,index)