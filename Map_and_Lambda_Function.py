cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    a = []
    if n==0:
        return a
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        a = [0,1]
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        return a

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))