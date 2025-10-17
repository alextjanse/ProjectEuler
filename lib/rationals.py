from math import gcd

class Rational:
    def __init__(self, nom: int, denom: int = 1):
        if denom == 0:
            raise ValueError(denom, "can't be zero")
        self.nom: int = nom // d
        self.denom: int = denom // d

    def __add__(self, other: "Rational"):
        return Rational(self.nom * other.denom + self.denom * other.nom, self.denom * other.denom)
    
    def __neg__(self):
        return Rational(-self.nom, self.denom)

    def __sub__(self, other: "Rational"):
        return self + (-other)
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.nom * other.nom, self.denom * other.denom)
        if isinstance(other, int):
            return Rational(other * self.nom, self.denom)
        return NotImplemented
    
    def __truediv__(self, other: "Rational"):
        return Rational(self.nom * other.denom, self.denom * other.nom)
    
    def __pow__(self, x: int):
        return Rational(self.nom ** x, self.denom ** x)
        
    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.nom * other.denom == self.denom * other.nom
        return False
    
    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.nom * other.denom != self.denom * other.nom
        return False

    def __lt__(self, other: "Rational"):
        return self.nom * other.denom < self.denom * other.nom
    
    def __le__(self, other: "Rational"):
        return self.nom * other.denom <= self.denom * other.nom
    
    def __ge__(self, other: "Rational"):
        return self.nom * other.denom >= self.denom * other.nom
    
    def __gt__(self, other: "Rational"):
        return self.nom * other.denom > self.denom * other.nom
    
    def normalize(self):
        g = gcd(self.nom, self.denom)
        self.nom //= g
        self.denom //= g

    def __float__(self):
        return self.nom / self.denom
    
    def __int__(self):
        if self.nom % self.denom != 0:
            print("rounding error")
        return self.nom // self.denom

    def __repr__(self):
        return f"Rational({self.nom}, {self.denom})"

r1 = Rational(127, 456)
r2 = Rational(6756, 124)
print(r1)
print(r2)

print("r1+r2", r1 + r2)
print("-r2", -r2)
print("r1-r2", r1 - r2)
print("r1*r2", r1 * r2)
print("r1/r2", r1 / r2)
