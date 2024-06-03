n ,m = map(int,input().split())

a = list(map(int,input().split()))
mp = {}

for i in range(n):
    if(a[i] in mp):
        mp[a[i]] += 1
    else:
        mp[a[i]] = 1

for  i in range(1,m+1,1):
    if(i in mp):
        print(mp[i])
    else:
        print(0)
        # print(mp)