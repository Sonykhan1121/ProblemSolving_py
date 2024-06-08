s = input()
st = set()
found  = False
for i in range(len(s)-1):
    if s[i]==s[i+1] and s[i].isalnum():
        print(s[i])
        found = True
        break
if not found :
    print(-1)