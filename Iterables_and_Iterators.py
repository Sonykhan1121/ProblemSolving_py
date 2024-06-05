import math 
n = int(input())
a = list(map(str,input().split()))
k = int(input())

acount = 0
for i in range(len(a)):
    if a[i] =='a':
        acount += 1
        
total = math.comb(n,k) -math.comb(n-acount,k)
# print(total)
ans = total/math.comb(n,k)
# print(ans)
print(f"{ans:.3f}")
