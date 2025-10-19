from math import isqrt
from fractions import Fraction
from lib.fractions import ContinuedFraction

# Source: https://en.wikipedia.org/wiki/Integer_square_root#continued_fraction_sqrt_Python
def continued_fraction_sqrt(n: int) -> ContinuedFraction:
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

if __name__ == "__main__":
    odds = 0
    for n in range(2, 10000 + 1):
        f = continued_fraction_sqrt(n)
        if len(f.period) & 1 == 1:
            odds += 1
    print(odds)