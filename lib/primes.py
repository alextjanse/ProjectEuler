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
    
    for p in primes():
        if p * p > n:
            break
        if n % p == 0:
            return False

    return True

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

if __name__ == "__main__":
    for i in range(100):
        if is_prime(i):
            print(i)