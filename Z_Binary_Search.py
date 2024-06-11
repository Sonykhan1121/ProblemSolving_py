import bisect
n , q = map(int,input().split())
a  = list(map(int,input().split()))
a.sort()
for i in range(q):
    value = int(input())
    now = bisect.bisect_left(a,value)
    if now != n and a[now] ==value:
        print("found")
    else:
        print("not found")