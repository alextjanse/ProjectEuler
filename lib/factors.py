from functools import reduce
from math import isqrt
import operator
from typing import Generator, Tuple
from .primes import primes
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

def phi_factors(factors: dict[int, int]) -> int:
    f = 1
    for p, n in factors.items():
        f *= p ** (n - 1) * (p - 1)
    return f

def get_factors(n_max: int, p_max = None) -> Generator[Tuple[int, Counter[int]], None, dict[int, Counter[int]]]:
    p_max = p_max or n_max
    factors: dict[int, Counter[int]] = defaultdict(Counter)
    number_pool: set[int] = set()
    for p in primes():
        if p > p_max:
            break

        for n in set(number_pool):
            if p * n > n_max:
                number_pool.remove(n)
                continue

            f = factors[n]
            i = n * p
            f_i = Counter(f)
            while i <= n_max:
                f_i[p] += 1
                factors[i] = Counter(f_i)
                number_pool.add(i)
                yield (i, f_i)
                i *= p
        
        f = Counter([p])
        n = p
        while n <= n_max:
            factors[n] = Counter(f)
            number_pool.add(n)
            n *= p
            
    return factors

if __name__ == "__main__":
    for n, fac in get_factors2(1000).items():
        print(n, fac)