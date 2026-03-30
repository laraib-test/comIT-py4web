# overload all operators 
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

from math import gcd


class Fraction:
    #constructor
    def __init__(self, num, den):
        self.num = num
        self.den = den 
        
        #operator(s) overloading
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __eq__(self, other):
        return self.num * other.den == other.num * self.den 
    
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.num * other.den < other.num * self.den
    
    def __gt__(self, other):
        return self.num * other.den > other.num * self.den
    
    def __repr__(self):
        return f"Fraction({self.num}/ {self.den})"
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(frac):
        common = gcd(frac.num, frac.den)
        return Fraction(frac.num // common, frac.den // common)


# Example usage
if __name__ == "__main__":
    a= Fraction(2, 3)
    b = Fraction(4, 5) 
    print(a, b)
    print(a + b)
    print(a * b)
    print(a - b)
    print(a / b)  
    print(a == b)
    print(a != b) 
    print(a < b)
    print(a > b)
    print(Fraction.simplify_fraction(Fraction(8, 12)))
    