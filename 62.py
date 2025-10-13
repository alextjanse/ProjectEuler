from collections import defaultdict

def get_digits(n):
    digits = [0] * 10
    for c in str(n):
        digits[int(c)] += 1
    return tuple(digits)

if __name__ == "__main__":
    cube_permutations = defaultdict(list)

    n = 1
    while True:
        digits = get_digits(n ** 3)
        cube_permutations[digits].append(n)

        if len(cube_permutations[digits]) == 5:
            print(cube_permutations[digits], cube_permutations[digits][0] ** 3)
            break

        n += 1