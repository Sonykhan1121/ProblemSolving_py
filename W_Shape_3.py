n = int(input())
space = n-1
star= 1
size = 2*n
for i in range(size): 
    for j in range(space):
        print(' ',end='')
    for j in range(star):
        print('*',end='')
    print()
    if(i<n-1):
        space-=1
        star+=2
    elif(i>n-1):
        space+=1
        star-=2