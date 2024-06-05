from collections import deque
tc = int(input())

while tc>0:
    n = int(input())
    now = deque(map(int,input().split()))
    # print(*now)
    last = 1<<31
    ok = True
    while len(now)>0:
        if last <now[0] or last <now[len(now)-1]:
            ok =  False
            break
        elif now[0]>=now[len(now)-1]:
            last = now.popleft()

        else:
            last = now.pop()
    


    if ok:
        print("Yes")
    else:
        print("No")


    tc-=1