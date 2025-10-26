from time import time
from lib.primes import is_prime

def f(x: int) -> int: return x ** 3 - 3 * x + 4
def R(p: int) -> int:
    r = 1
    for x in range(p):
        r *= f(x)
        r %= p
    return r

def solve():
    R_sum = 0
    for p in range(10 ** 9, 10 ** 9 + 10 ** 8):
        if not is_prime(p):
            continue
        R_p = R(p)
        print(p, R_p)
        R_sum += R_p
    
    return R_sum

if __name__ == "__main__":
    print(solve())