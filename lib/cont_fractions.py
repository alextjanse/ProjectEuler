from fractions import Fraction
from math import isqrt

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
    
# Source: https://en.wikipedia.org/wiki/Integer_square_root#continued_fraction_sqrt_Python
def sqrt_continued_fraction(n: int) -> ContinuedFraction:
    a0 = isqrt(n)

    if a0 * a0 == n:
        return ContinuedFraction(0, [])
    
    m, d, a = 0, 1, a0
    period = []
    seen = set()

    while True:
        m_next = d * a - m
        d_next = (n - m_next * m_next) // d
        a_next = (a0 + m_next) // d_next

        if (m_next, d_next, a_next) in seen:
            break
    
        seen.add((m_next, d_next, a_next))
        period.append(a_next)
        m, d, a = m_next, d_next, a_next
    
    return ContinuedFraction(a0, tuple(period))
