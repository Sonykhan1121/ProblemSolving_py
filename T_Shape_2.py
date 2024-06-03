n = int(input())
space = n-1
star = 1
for i in range(n):
    for j in range(space):
        print(' ',end='')
    for j in range(star):
        print('*',end='')
    print()
    space-=1
    star+=2
    
