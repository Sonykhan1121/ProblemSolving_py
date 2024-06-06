def compare(c):
    if c.islower():
        return (0,c,c)
    elif c.isupper():
        return (1,c,c)
    elif c.isdigit():

        return (3 if int(c)%2==0 else 2,c,c)
s = input()
ans = sorted(s,key = compare)
print("".join(ans),end='')