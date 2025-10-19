from lib.cont_fractions import sqrt_continued_fraction

if __name__ == "__main__":
    odds = 0
    for n in range(2, 10000 + 1):
        f = sqrt_continued_fraction(n)
        if len(f.period) & 1 == 1:
            odds += 1
    print(odds)