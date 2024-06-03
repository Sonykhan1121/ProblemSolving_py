a , b, c =map(int,input().split())
m  = min(a,b,c)
res=m
a-=m
b-=m
c-=m
res+=(min(a//2,c))
print(res)