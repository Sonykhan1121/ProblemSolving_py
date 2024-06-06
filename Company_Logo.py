def compare(item):
    key, value = item
    return -value,key
s = input()

size = len(s)

mp = {}
for i in s:
    mp[i] = mp.get(i,0)+1
# print(mp)

now = sorted(mp.items(),key=compare)
# print(type(now))
for i in range(3):
    print(now[i][0],now[i][1])
