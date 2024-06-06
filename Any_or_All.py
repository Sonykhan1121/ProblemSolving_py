n = int(input())
a = list(map(int,input().split()))
# print(any(a))
print((all(i>0 for i in a) and any(True for i in a if str(i)==str(i)[::-1])))