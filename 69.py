from lib.primes import prime_factors
from fractions import Fraction

def phi(n: int) -> int:
    x = 1
    for p, m in prime_factors(n).items():
        x *= p ** (m - 1) * (p - 1)
    return x

def solve():
    n_max, n_phi_max = 0, 0

    for n in range(2, 10**6 + 1):
        n_phi = n / phi(n)
        if n_phi > n_phi_max:
            n_max, n_phi_max = n, n_phi
    
    print(n_max, n_phi_max)

if __name__ == "__main__":
    solve()