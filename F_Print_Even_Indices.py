
n = int(input())
a = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    if(i%2==0):
        print(a[i],end=' ')
