from math import isqrt
from lib.cont_fractions import ContinuedFraction, sqrt_continued_fraction

def is_square(n: int) -> bool:
    root = isqrt(n)
    return root * root == n

def solve(D = 1000):
    x_max, d_max = 0, 0

    for d in range(1, D + 1):
        if is_square(d):
            continue

        frac = sqrt_continued_fraction(d)

        period_length = len(frac.period)
        
        solution = frac.value(period_length) if period_length % 2 == 0 else frac.value(2 * period_length)

        x = solution.numerator
        
        if x > x_max:
            x_max, d_max = x, d
    
    print(d_max, x_max)

if __name__ == "__main__":
    solve()