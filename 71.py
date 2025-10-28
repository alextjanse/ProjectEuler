from math import ceil

'''
p / q: query frac
n / d, st. p / q < n / d => pd < qn
Observation: in example, pd + 1 = qn for right nbs -> n = (pd + 1) / q
n_min, d_min, where for all n, d: n_min / d_min < n / d -> n_min * d < n * d_min
'''

def solve(p, q, d_max=10**6):
    n_min, d_min = float('inf'), 1
    for d in range(2, d_max + 1):
        n = ((p * d + 1) * q) // (q ** 2) # Prevent rounding errors
        if n * d_min < n_min * d:
            n_min, d_min = n, d
    return n_min, d_min

if __name__ == "__main__":
    print(solve(2, 5, 8))
    print(solve(2, 5, 9))
    print(solve(3, 7, 10**6))