n = int(input())
a = list(map(int, input().split()))
count =0
for i in a:
    if i+1 in a:
        count+=1
print(count)