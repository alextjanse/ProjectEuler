from math import isqrt

def is_square(n: int) -> bool:
    root = isqrt(n)
    return root * root == n

def solve(d_max = 1000):
    not_found_ds = { d for d in range(1, d_max + 1) if not is_square(d) }
    
    x = 2
    while not_found_ds:
        for d in set(not_found_ds):
            dy2 = x * x - 1
            if dy2 % d == 0 and is_square(dy2 // d):
                y = isqrt(dy2 // d)
                print(x, d, y, ':', x * x, '-', d, y * y, '=', 1, ';', len(not_found_ds) - 1, 'remaining')

                not_found_ds.remove(d)
        x += 1

    print(x)

if __name__ == "__main__":
    solve()