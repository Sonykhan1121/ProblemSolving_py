n = int(input())

a = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
for i in range(n):
    print(a[i],end=' ')