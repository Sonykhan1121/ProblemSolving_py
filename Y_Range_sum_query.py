import itertools 
n , q= map(int,input().split())

a  = list(map(int,input().split()))
prefix  = list(itertools.accumulate(a))
print(*prefix)
for i in range(q):
    l , r = map(int, input().split())
    l-=1
    r-=1
    ans = prefix[r]
    if(l>0):
        ans-=prefix[l-1]
    print(ans)
