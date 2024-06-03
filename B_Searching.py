n = int(input())
a = list(map(int,input().split()))
value = int(input())
ans = -1
for i in range(n):
    if(a[i] == value):
        ans = i;
        break
print(ans)