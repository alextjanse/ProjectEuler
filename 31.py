def solve():
    counter = 0

    states = [(200, [1, 2, 5, 10, 20, 50, 100, 200])]

    while states:
        rem, coins = states.pop()

        if rem == 0:
            counter += 1
            continue

        if len(coins) == 0:
            # no coins remaining, but there is a remainder
            continue

        coin = coins.pop()
        n = 0
        while n * coin <= rem:
            states.append((rem - n * coin, list(coins)))
            n += 1

    return counter

if __name__ == "__main__":
    print(solve())