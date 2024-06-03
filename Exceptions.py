n = int(input())
while n>0:
    first , second = map(str,input().split())

    try:
        print(int(first) // int(second))
    except Exception as e:
        print("Error Code: "+str(e))

    n-=1