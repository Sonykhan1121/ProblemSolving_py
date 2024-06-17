def wrapper(f):
    def fun(l):
        ans_list = []
        for i in l:
            ans_list.append(f"+91 {i[-10:-5]} {i[-5:]}")
        f(ans_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


