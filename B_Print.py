def p(n):
    for i in range(1,n+1):
        print(i,end='')
        if(i!=n):
            print(' ',end='')

n = int(input())
p(n)
