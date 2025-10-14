f = open('data/0067_triangle.txt', 'r')
lines = f.readlines()

accum_sums = list(map(int, lines[-1].split(' ')))

for line in lines[-2::-1]:
    new_accum_sums = []
    for n, a, b in zip(map(int, line.split(' ')), accum_sums[:-1], accum_sums[1:]):
        new_accum_sums.append(n + max(a, b))
    accum_sums = new_accum_sums

print(accum_sums[0])