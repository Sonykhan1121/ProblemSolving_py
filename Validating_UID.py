n = int(input())
while n> 0:
    now = input()
    upper_case = lower_case =digit =alpha_num =0
    st = set()
    duplicate = False
    for c in now:
        if c.isupper():
            upper_case+=1
        elif c.islower():
            lower_case+=1
        elif c.isdigit():
            digit+=1
        if c.isalnum():
            alpha_num+=1 
        if c in st:
            duplicate = True
            break
        else:
            st.add(c)
    # assert len(now)!=10
    # assert duplicate
    # assert alpha_num!=10
    # assert upper_case<2
    # assert digit<3 
    if len(now)!=10 or duplicate:
        # print(1)
        print("Invalid")
    elif alpha_num!=10:
        # print(2)
        print("Invalid")
    elif upper_case<2 or digit<3:
        # print(3)
        print("Invalid")
    else:
        print("Valid")
    


    n-=1