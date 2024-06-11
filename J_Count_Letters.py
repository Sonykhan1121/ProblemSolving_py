s = input()

mp = dict()
# print(type(mp))
for i in s:
    if i not in mp:
        mp[i]= 1
    else:
        mp[i]+= 1

for i in range(26):
    c = chr(i+97)
    if c in mp:
        print(f"{c} : {mp[c]}")