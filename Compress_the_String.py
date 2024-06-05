s = input()
prev = s[0]
count =1
for i in range(1,len(s)):
    if s[i] ==prev:
        count+=1
    else:
        print(f"{count, int(prev)}",end=' ')
        prev = s[i]
        count = 1
print(f"{count, int(prev)}")