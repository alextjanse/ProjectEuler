from lib.cont_fractions import ContinuedFraction

def solve():
    a0 = 2

    period = []
    k = 2
    while len(period) < 100:
        period += [1, k, 1]
        k += 2
    
    f = ContinuedFraction(a0, period)

    value = f.value(100)

    i = value.numerator
    s = 0
    while i > 0:
        s += i % 10
        i //= 10

    print(s)

if __name__ == "__main__":
    solve()