s = str(input())

for i in range(len(s)):
    if(s[i] == ','):
        print(" ",end='')
    elif(s[i]>='a' and s[i]<='z'):
        print(s[i].upper(), end='')
    else:
        print(s[i].lower(),end='')