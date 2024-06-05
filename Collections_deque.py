from collections import deque
n = int(input())
ans = deque()
for i in range(n):
    now = list(map(str,input().split()))
    size = len(now)
    if size ==2:
        if now[0]=='append':
            ans.append(int(now[1]))
        elif now[0]=='appendleft':
            ans.appendleft(int(now[1]))
    elif size ==1:
        if now[0]=='pop':
            ans.pop()
        else:
            ans.popleft()

print(*ans)