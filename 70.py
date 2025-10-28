from lib.primes import primes
from lib.factors import get_factors,phi_factors
from collections import Counter, defaultdict

def digits(n: int) -> Counter[int]:
    return Counter((int(c) for c in str(n)))

def solve():
    min_n, min_ratio = 0, float('inf')
    
    for i, (n, factors) in enumerate(get_factors(10**7, 10**7 // 2)):
        phi_n = phi_factors(factors)
        if digits(n) == digits(phi_n):
            print(i, n, phi_n, factors)
            if n / phi_n < min_ratio:
                print('opt')
                min_n, min_ratio = n, n / phi_n
    return min_n

if __name__ == "__main__":
    print(solve())