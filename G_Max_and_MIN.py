def min_max(a):
    min = a[0]
    max = a[0]
    for i in range(1,len(a)):
        if(a[i]<min):
            min = a[i]
        if(a[i]>max):
            max = a[i]
        
    return min,max
    

n = int(input())
a = list(map(int, input().split()))

min ,max =min_max(a)
print(min,max)