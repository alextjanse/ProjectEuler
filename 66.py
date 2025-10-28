from math import isqrt
from lib.cont_fractions import sqrt_continued_fraction

def is_square(n: int) -> bool:
    root = isqrt(n)
    return root * root == n

def solve(D: int = 1000) -> int:
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
    
    return d_max

if __name__ == "__main__":
    print(solve())