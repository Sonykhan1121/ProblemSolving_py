n = int(input())

mp  = {}
a = []
for i in range(n):
    a.append(input())
    if a[i] not in mp:
        mp[a[i]] =1
    else:
        mp[a[i]] +=1
    
print(len(mp))
for i in a:
    if mp[i]>0:
        print(mp[i],end=' ')
        mp[i] =0
print()