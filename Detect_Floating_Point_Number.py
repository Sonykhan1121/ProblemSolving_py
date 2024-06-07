tc = int(input())
for i in range(tc):
    s = input()
    try:
        if '.' not in s:
            s+='a'
        now = float(s)
    except ValueError :
        print("False")
    else:
        print("True")
