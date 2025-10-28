from functools import reduce
from math import isqrt
import operator
from primes import primes
from collections import Counter, defaultdict

def factorize(n: int) -> dict[int, int]:
    factors: Counter[int] = Counter()

    for p in primes():
        if n == 1:
            break

        while n % p == 0:
            factors[p] += 1
            n //= p

    return factors

def reduce_factors(factors: dict[int, int]) -> int:
    return reduce(operator.mul, map(lambda f: f[0] ** f[1], factors.items()), 1)

def phi(n: int) -> int:
    if n < 1: raise ValueError(n, "has to be larger than 0")
    elif n == 1: return 1
    x = 1
    for p, m in factorize(n).items():
        x *= p ** (m - 1) * (p - 1)
    return x

'''
Get the prime factors of all numbers up to n.
'''
def get_factors(n: int) -> dict[int, Counter[int]]:
    factors: dict[int, Counter[int]] = defaultdict(Counter)

    active_numbers: set[int] = set()
    root_n = isqrt(n)
    for p in primes():
        if p > n:
            break
        for i in set(active_numbers):
            fac_n = factors[i]
            if i * p > n:
                # next p will also be bigger than max, remove it
                active_numbers.remove(i)
                continue

            new_factors = Counter(fac_n)
            j = i * p
            while j <= n:
                new_factors[p] += 1
                factors[j] = Counter(new_factors) # Copy
                active_numbers.add(j)
                j *= p

        # add p and powers of p
        new_factors = Counter([p])
        i = p
        while i <= n:
            factors[i] = Counter(new_factors)
            active_numbers.add(i)
            i *= p
            new_factors[p] += 1

    return factors

if __name__ == "__main__":
    for n, fac in get_factors(1000).items():
        print(n, fac)