import re

tc = int(input())
while tc >0:
    s = input()
    if re.match(r"^(7|8|9)[0-9]{9}$",s):
        print("YES")
    else:
        print("NO") 


    tc-=1