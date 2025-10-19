from math import isqrt
# from gmpy2 import is_square

def is_square(n: int) -> bool:
    root = isqrt(n)
    return root * root == n

def solve(d_max: int = 1000) -> int:
    ds = { d for d in range(1, d_max + 1) if not is_square(d) }

    x2_max, d_max, y = 0, 0, 1
    while ds:
        for d in set(ds):
            x2 = (d * y * y) + 1
            if is_square(x2):
                ds.remove(d)
                print(isqrt(x2), '-', d, y, len(ds))
                if x2 > x2_max:
                    x2_max, d_max = x2, d
        y += 1
    
    y2_max = (x2_max - 1) // d_max
    print(isqrt(x2_max), d_max, isqrt(y2_max), x2_max, y2_max, x2_max - d_max * y2_max)

    return isqrt(x2_max)

if __name__ == "__main__":
    solve()