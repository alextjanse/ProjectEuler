from typing import Any, Callable

def bin_search(array: list, item, lb: int = 0, ub: int = -1):
    if ub == -1:
        ub = len(array)
    if ub - lb < 1:
        return array[lb] == item
    
    m = (ub + lb) // 2
    if item < array[m]:
        return bin_search(array, item, lb, m)
    elif m == array[m]:
        return True
    else:
        return bin_search(array, item, m, ub)