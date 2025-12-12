import math
class RationalFraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        result = RationalFraction(new_num, new_den)
        result.reduce()
        return result

    def __iadd__(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator *= other.denominator
        self.reduce()
        return self
    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        result = RationalFraction(new_num, new_den)
        result.reduce()
        return result

    def __isub__(self, other):

        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator *= other.denominator
        self.reduce()
        return self

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        result = RationalFraction(new_num, new_den)
        result.reduce()
        return result

    def __imul__(self, other):

        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.reduce()
        return self

    def __truediv__(self, other):

        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        result = RationalFraction(new_num, new_den)
        result.reduce()
        return result
    
    def __itruediv__(self, other):

        self.numerator *= other.denominator
        self.denominator *= other.numerator
        self.reduce()
        return self
