import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        new_real = self.real +no.real
        new_imaginary = self.imaginary +no.imaginary
        return Complex(new_real, new_imaginary)
    def __sub__(self, no):
        new_real = self.real -no.real
        new_imaginary = self.imaginary -no.imaginary
        return Complex(new_real, new_imaginary)
    def __mul__(self, no):
        new_real = self.real*no.real - self.imaginary*no.imaginary
        new_imaginary = self.real*no.imaginary+ self.imaginary*no.real
        return Complex(new_real, new_imaginary)
    def __truediv__(self, no):
        
        down = no.real**2 + no.imaginary**2
        new_c = self * Complex(no.real, -no.imaginary)

        return Complex(new_c.real/down, new_c.imaginary/down)
    def mod(self):
        return Complex(math.sqrt(self.real**2+self.imaginary**2),0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    # print(*c)
    # print(*d)
    x = Complex(*c)
    y = Complex(*d)
    # print(x,y)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')