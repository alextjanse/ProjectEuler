'''Prime module, with different functions for prime calculations.'''

from collections import Counter
from functools import reduce
import operator

prime_list = [2, 3]
prime_set = set(prime_list)

def is_prime(n: int) -> bool:
    p_max = prime_list[-1]
    
    if n <= p_max:
        return n in prime_set
    
    if p_max * p_max >= n:
        for p in prime_list:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True
    
    prime_gen = next_prime()
    while p_max < n:
        p_max = next(prime_gen)
    
    return p_max == n

def next_prime():
    p = prime_list[-1] + 2
    while True:
        if is_prime(p):
            prime_list.append(p)
            prime_set.add(p)
            yield p
        p += 2

def primes():
    for p in prime_list:
        yield p
    
    for p in next_prime():
        yield p

def prime_factors(n: int) -> dict[int, int]:
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
    for p, m in prime_factors(n).items():
        x *= p ** (m - 1) * (p - 1)
    return x

if __name__ == "__main__":
    factors = prime_factors(12345)
    print(factors)
    print(reduce_factors(factors))