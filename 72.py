from lib.factors import get_factors, phi_factors

def solve(d_max = 10**6):
    s = 0
    for _, fac in get_factors(d_max).items():
        s += phi_factors(fac)
    return s

if __name__ == "__main__":
    print(solve())