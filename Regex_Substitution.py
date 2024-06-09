import re
n = int(input())

for i in range(n):
    s = input()
    res = re.sub(r'(?<=\s)&&(?=\s)',"and",s)
    res = re.sub(r'(?<=\s)\|\|(?=\s)',"or",res)
    print(res)