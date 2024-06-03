n = int(input())
sum =0
list = list(map(int,input().split()))
for i in range(n):
    sum = sum + list[i]
if(sum<0):
    sum = -sum
print(sum)
