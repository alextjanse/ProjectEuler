from math import ceil, gcd

'''
a / b: lower bound
p / q: upper bound

for d: for n:
a / b < n / d < p / q

a / b < n / d -> a * d < b * n
n / d < p / q -> n * q < p * d

n_min = ceil((a * d + 1) / b)
n_max = (p * d - 1) // q

valid if n in [n_min, n_max] gcd(n, d) == 1
'''

def solve(d_max = 12000, lb = (1, 3), ub = (1, 2)):
    a, b = lb
    p, q = ub
    count = 0
    for d in range(2, d_max + 1):
        n_min = ceil((a * d + 1) / b)
        n_max = (p * d - 1) // q
        for n in range(n_min, n_max + 1):
            if gcd(n, d) == 1:
                count += 1
    return count

if __name__ == "__main__":
    print(solve())