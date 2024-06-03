def p(n):
    if(n==0):
        return
    print(n,end='')
    if(n!=1):
        print(' ',end='')
    p(n-1)

n = int(input())
p(n)