import re
tc = int(input())
full_code =""
while tc >0:
    now = input()
    # print(now)
    full_code+= " "+now
    
    tc-=1

# print(full_code)

temp = re.findall(r"\{([^}]*)\}",full_code)
# print(len(temp))
for i in temp:
    now = list(map(str,re.split(r"[\s:;,()]",i)))
    for j in now:
        if len(j)==4 or len(j)==7:
            if re.match(r"^#([A-Fa-f0-9]{3})|([A-Fa-f0-9]{6})$",j):
                print(j)
