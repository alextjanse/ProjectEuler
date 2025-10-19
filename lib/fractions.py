from fractions import Fraction

class ContinuedFraction:
    def __init__(self, a0, period) -> None:
        self.a0: int = a0
        self.period: list[int] = period
    
    def value(self, n: int) -> Fraction:
        # Return the value of the continued fraction truncated to n terms
        if n <= 0 or len(self.period) == 0:
            return Fraction(self.a0)
        # build coefficient list: a0 followed by n-1 terms from the repeating period
        coeffs = [self.a0] + [self.period[(i) % len(self.period)] for i in range(n - 1)]
        # evaluate from the back: last coeff, then iterate reversed
        val = Fraction(coeffs[-1])
        for c in reversed(coeffs[:-1]):
            val = Fraction(c) + Fraction(1, 1) / val
        return val