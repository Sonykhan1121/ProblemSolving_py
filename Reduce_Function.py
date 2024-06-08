from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(1,1)
    for f in fracs:
        t*=f
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    # print(fracs)
    result = product(fracs)
    print(*result)