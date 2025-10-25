from lib.primes import prime_factors, phi
from fractions import Fraction

def solve():
    n_max, n_phi_max = 0, 0

    for n in range(2, 10**6 + 1):
        n_phi = n / phi(n)
        if n_phi > n_phi_max:
            n_max, n_phi_max = n, n_phi
    
    print(n_max, n_phi_max)

if __name__ == "__main__":
    solve()