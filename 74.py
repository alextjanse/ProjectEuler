from math import factorial

def digit_factorial(n: int) -> int:
    return sum(map(lambda c: factorial(int(c)), str(n)))

def solve():
    # Looping numbers. If found, end chain with loop once
    l_2 = { 871, 45361, 872, 45352 }
    l_3 = { 169, 363601, 1454 }

    lengths: dict[int, int] = {
        0: 2, # 0 -> 1 -> 1
        1: 1, # 1 -> 1
        2: 1, # 2 -> 2
        145: 1, # 145 -> 145
        40585: 1, # 40585 -> 40585, found while debugging
    } | { i : 2 for i in l_2 } | { i : 3 for i in l_3 }

    count = 0

    for s in range(3, 10**6 + 1):
        if s in lengths:
            continue
        t = s
        chain = [s]
        while t not in lengths:
            r = digit_factorial(t)
            chain.append(r)
            t = r
        length_t = lengths.get(t, 1)
        for i, t in enumerate(chain[::-1]):
            lengths[t] = length_t + i
        if lengths[s] == 60:
            count += 1

    return count

if __name__ == "__main__":
    print(solve())