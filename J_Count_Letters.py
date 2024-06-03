s = str(input())
n  = len(s)
mp = {}

for i in range(n):
    if(s[i] in mp):
        mp[s[i]]+=1
    else:
        mp[s[i]]=1

for i in range(ord('a'),ord('z')+1):
    ch = chr(i)
    if(ch in mp):
        print(f"{ch} : {mp[ch]}")