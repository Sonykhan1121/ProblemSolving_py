n , m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
value = int(input())
found = False
for i in range(n):
    for j in range(m):
        if(a[i][j]==value):
            found = True
            break
if(found):
    print("will not take number")
else:
    print("will take number")