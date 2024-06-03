a = int(input())
first = a//10
second =a%10
if(first==0 or second==0 or (first%second==0) or (second % first ==0)):
    print("YES")
else:
    print("NO")
