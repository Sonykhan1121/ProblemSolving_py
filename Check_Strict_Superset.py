main_set = set(map(int,input().split()))
n = int(input())
okay = True
for i in range(n):
    setA =(set(map(int,input().split())))
    if not main_set.issuperset(setA) or len(setA)>=len(main_set):
        okay = False
if okay :
    print("True")
else:
    print("False")
