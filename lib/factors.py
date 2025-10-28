from functools import reduce
from math import isqrt
import operator
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

def get_factors(n_max: int) -> dict[int, Counter[int]]:
    factors: dict[int, Counter[int]] = defaultdict(Counter)

    new_numbers: dict[int, Counter[int]] = defaultdict(Counter)
    for p in primes():
        if p > n_max: break
        for n, f in factors.items():
            if p > n_max: break
            i = n * p
            f_i = Counter(f)
            while i <= n_max:
                f_i[p] += 1
                new_numbers[i] = Counter(f_i)
                i *= p
        factors.update(new_numbers)
        new_numbers.clear()
        
        f = Counter([p])
        n = p
        while n <= n_max:
            factors[n] = Counter(f)
            n *= p
            

    return factors

if __name__ == "__main__":
    for n, fac in get_factors2(1000).items():
        print(n, fac)