def r(n):
    if(n==0):
        return
    print("I love Recursion")
    r(n-1)

n = int(input())
r(n)
