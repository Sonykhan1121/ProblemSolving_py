from collections import OrderedDict
n = int(input())
mp = OrderedDict()
for i in range(n):
    s = list(map(str,input().split()))
    size = len(s)
    name = ""
    for i in range(size-1):
        name = name + s[i] 
        if i!=size-1:
            name+=" "
    price = int(s[size-1])

    if name not in mp:
        mp[name] = price
    else:
        mp[name]+=price
for i,j in mp.items():
    print(i+""+str(j))
