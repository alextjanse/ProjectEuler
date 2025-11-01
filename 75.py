from collections import defaultdict
from math import isqrt

def solve():
    lengths = defaultdict(set)
    m_max = (-1 + isqrt(1 + 4 * 750000)) // 2 # quadratic equation
    for m in range(2, m_max + 1):
        for n in range(m - 1, 0, -1):
            a = m * m - n * n
            b = 2 * n * m
            c = n * n + m * m
            if a > b:
                a, b = b, a
            L = a + b + c
            if (a, b, c) in lengths[L]:
                continue
            i, j, k = a, b, c
            while L <= 1500000:
                lengths[L].add((i, j, k))
                i += a
                j += b
                k += c
                L = i + j + k

    return sum((1 if len(lengths[l]) == 1 else 0 for l in lengths)) 

if __name__ == "__main__":
    print(solve())