s = str(input())
i=0
j=len(s)-1
find = True
while i<j:
    if(s[i]!=s[j]):
        find = False
        break
    i+=1
    j-=1
if(find):
    print("YES")
else:
    print("NO")


