'''Prime module, with different functions for prime calculations.'''

primes = [2, 3]

def is_prime(n: int) -> bool:
    p_max = primes[-1]
    
    if n <= p_max:
        return n in primes
    
    if p_max * p_max >= n:
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    for p in next_prime():
        if p < n:
            continue
        return p == n
    
    return False

def next_prime():
    candidate = primes[-1] + 2
    while True:
        if is_prime(candidate):
            primes.append(candidate)
            yield candidate
        candidate += 2

def get_primes():
    for p in primes:
        yield p
    
    for p in next_prime():
        yield p