'''
p / q: query frac
n / d, st. n / d < p / q => qn < pd
Observation: in example, pd = qn + 1 for nbs -> n = (pd - 1) / q
If round down, it holds qn < pd
Find opt n,d
'''

def solve(p = 3, q = 7, d_max = 10**6):
    n_opt, d_opt = 0, 1
    for d in range(2, d_max + 1):
        if d == q: 
            continue
        n = (p * d - 1) // q
        if n * d_opt > n_opt * d:
            n_opt, d_opt = n, d
    return n_opt, d_opt

if __name__ == "__main__":
    print(solve())