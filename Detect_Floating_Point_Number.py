tc = int(input())
for i in range(tc):
    s = input()
    try:
        now = float(s)
    except ValueError :
        print("False")
    else:
        print("True")
