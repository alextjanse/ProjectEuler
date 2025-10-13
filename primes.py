'''Prime module, with different functions for prime calculations.'''

def sieve(n):
    '''Get primes up to the given number.'''
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    primes = []
    for p, prime in enumerate(sieve):
        if not prime:
            continue
        primes.append(p)
        for q in range(p, n + 1, p):
            sieve[q] = False
    
    return primes

def is_prime(p):
    '''Check whether the given number is a prime.'''
    if p % 2 == 0:
        return False
    i = 3
    while i * i <= p:
        if p % i == 0:
            return False
        i += 2
    return True
