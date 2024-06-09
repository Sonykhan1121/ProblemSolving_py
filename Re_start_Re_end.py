import re
s = input()
word = input()

ans = re.finditer(f"(?={word})",s)
pp = True
for i in ans:
    pp = False
    print(tuple([i.start(),i.start()+len(word)-1]))
# print()
if pp:
    print((-1,-1))
    
