from lib.primes import primes
from collections import Counter, defaultdict

def digits(n: int) -> Counter[int]:
    return Counter((int(c) for c in str(n)))

def phi_factors(factors: dict[int, int]) -> int:
    f = 1
    for p, n in factors.items():
        f *= p ** (n - 1) * (p - 1)
    return f

def solve():
    min_n, min_ratio = 0, float('inf')
    
    numbers: dict[int, Counter] = defaultdict(Counter)

    for p in primes():
        if p > 10**7 // 2:
            break

        new_numbers: dict[int, Counter] = defaultdict(Counter)
        remove_numbers: set[int] = set()
        
        for n, factors in numbers.items():
            if n * p > 10**7:
                # next p will also be bigger than max, remove it
                remove_numbers.add(n)
                continue

            new_factors = Counter(factors)
            m = n * p
            while m < 10**7:
                new_factors[p] += 1
                phi_m = phi_factors(new_factors)
                if digits(m) == digits(phi_m):
                    print(m, new_factors)
                    if m / phi_m < min_ratio:
                        print('opt')
                        min_n, min_ratio = m, m / phi_m
                new_numbers[m] = Counter(new_factors) # Copy
                m *= p
        
        # update numbers
        for n in remove_numbers:
            numbers.pop(n)
        numbers.update(new_numbers)

        # add p and powers of p
        new_factors = Counter([p])
        n = p
        while n < 10**7:
            numbers[n] = Counter(new_factors)
            new_factors[p] += 1
            n *= p

    return min_n

if __name__ == "__main__":
    print(solve())