tc = int(input())
while tc > 0:
    now = input()
    if now[0] not in "456":
        print("Invalid")
        tc-=1
        continue

    if '-' in now:
        a = list(now.split('-'))
        if len(a)!=4:
            print("Invalid")
            tc-=1
            continue
        size =True
        for i in a:
            if len(i)!=4:
                print("Invalid")
                size = False
                break
        if not size:
            tc-=1
            continue
        now = "".join(a)
    # print("value : ",now)
    if len(now)!=16:
        print("Invalid")
        tc-=1
        continue
    con  = True
    for i in now:
        if i.isdigit():
            pass
        else:
            print("Invalid")
            con = False
            break
    if not con:
        tc-=1
        continue
    concecutive =False
    for i in range(len(now)):
        test = now[i]
        total = 1
        while i+1 <len(now) and test == now[i+1]:
            i+=1
            total+=1
        if total > 3:
            print("Invalid")
            concecutive = True
            break
    if  concecutive:
        tc-=1
        continue
    print("Valid")

    tc-=1