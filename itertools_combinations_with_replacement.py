import itertools
s , k =map(str,input().split())
k = int(k)

now =(list(itertools.combinations_with_replacement(sorted(s),k)))
for i in now:
    print(''.join(i))

