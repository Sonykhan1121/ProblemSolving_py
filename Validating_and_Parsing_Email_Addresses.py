import re
tc = int(input())

while tc > 0:
    name , email_i = map(str,input().split())
    email = email_i[1:-1]
    # print(name+" "+email)
    username=domain_extension = ""
    if '@' in email:
        multi = list(map(str,email.split('@')))
        if len(multi)!=2:
            tc-=1
            continue
        username, domain_extension = email.split('@')
    else:
        tc-=1
        continue

    # print(username,domain_extension)
    first = last = ""
    if '.' in domain_extension:
        multi = list(map(str,domain_extension.split('.')))
        if len(multi)!=2:
            tc-=1
            continue
        first, last = domain_extension.split('.')
    # print(first,last)
    # print(username[0].isalpha())
    # print(username.isalnum())
    # print(first.isalpha())
    # print(last.isalpha())
    # print(len(last))
    if username[0].isalpha() and (re.search(r'[a-zA-Z0-9_-]',username))  and first.isalpha() and last.isalpha() and len(last) >=1 and len(last)<=3:
        print(name,email_i)
    

    tc-=1