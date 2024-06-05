from itertools import combinations
s , k = map(str,input().split())

# print(list(combinations(s,int(k))))
result = []
for i in range(1,int(k)+1):
    result.extend(list(combinations(sorted(s),int(i))))
# print(result)
for i in result:

    for j in i:
        print(j,end='')
    print()