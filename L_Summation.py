def sum(a,i):
    if(i==-1):
        return 0
    return a[i]+sum(a,i-1)

n = int(input())
a = list(map(int,input().split()))
ans = sum(a,n-1)
print(ans)