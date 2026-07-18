# Whats happening? -> creation of own data type for fraction

class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):          # __str__ is a magic method
        return"{}/{}".format(self.num,self.den)

from Day6 import Fraction
f1=Fraction(3,4)
type(f1)
print(f1)