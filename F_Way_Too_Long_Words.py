tc = int(input())

for i in range(tc):
    now = str(input())
    size = len(now)
    if(size>10):
        print(f"{now[0]}{size-2}{now[size-1]}")
    else:
        print(now)
