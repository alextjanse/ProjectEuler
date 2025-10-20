
'''
A 16-digit string must have the number 10 in the
outer ring. We can now fix the arrangements of the
values in a list with fixed indexing.

The index triplets are:
0, 1, 2
3, 2, 4
5, 4, 6
7, 6, 8
9, 8, 1

Now we just need to check over all possible solutions using DFS.
'''

from functools import reduce
import operator
from typing import Tuple

index_triplets = [
    (0, 1, 2),
    (3, 2, 4),
    (5, 4, 6),
    (7, 6, 8),
    (9, 8, 1),
]

def get_triplet(solution: list[int], triplet: Tuple[int, int, int]) -> Tuple[int, int, int]:
    i,j,k = triplet
    return solution[i], solution[j], solution[k]

def check_solution(solution: list[int]) -> bool:
    if 10 in map(lambda i: solution[i], [1, 2, 4, 6, 8]):
        return False

    target = None
    for triplet in index_triplets:
        # First triplet should be the first one in order
        if solution[triplet[0]] != 0 and solution[0] > solution[triplet[0]]:
            return False
        
        p = reduce(operator.mul, get_triplet(solution, triplet), 1)
        if p == 0:
            continue
        
        s = sum(map(lambda i: solution[i], triplet))
        if target is None:
            target = s
        elif s != target:
            return False
    
    return True

def get_target(solution: list[int]) -> int | None:
    for triplet in index_triplets:
        values = get_triplet(solution, triplet)
        if reduce(operator.mul, values, 1) == 0:
            continue
        # solution should be correct, so first sum value is the target
        return sum(values)

    return None

def stringify(solution: list[int]) -> int:
    s = ""
    for i, j, k in index_triplets:
        s += str(solution[i]) + str(solution[j]) + str(solution[k])

    return int(s)

def solve():
    start_solution = [0] * 10

    max_value = 0
    '''
    State:
    - Array with the values filled in. Empty values are 0,
      so if multiplying a triplet equals 0, the triplet isn't
      filled in yet.
    - Set of numbers that haven't been used.
    - List of triplets that haven't been filled in.
    '''
    queue = [(start_solution, set(range(1, 11)))]
    while queue:
        solution, numbers = queue.pop()

        if len(numbers) == 0:
            value = stringify(solution)
            max_value = max(max_value, value)
            continue

        i = solution.index(0)
        for n in numbers:
            new_solution = solution[:]
            new_solution[i] = n
            if check_solution(new_solution):
                queue.append((new_solution, numbers - {n}))
    
    print(max_value)

if __name__ == "__main__":
    solve()