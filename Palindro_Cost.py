tc = int(input())

while tc >0:
    s , have = map(str,input().split())
    have = int(have)
    left ,right = 0,len(s)-1
    need =0
    while left <right:
        if s[left]!=s[right]:
            dif = abs(ord(s[left])-ord(s[right]))
            need+=dif
        left+=1
        right-=1

    if have >=need:
        print("YES")
    else:
        print("NO")
    tc-=1