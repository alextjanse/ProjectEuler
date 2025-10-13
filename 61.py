from typing import Tuple
from collections import defaultdict

Fig = Tuple[int, int]


def figurate(n: int, s: int): return n * ((s - 2) * n - (s - 4)) // 2

ss = range(3, 9)
fs = {s: set() for s in ss}

def pq(f: int) -> Tuple[int, int]: return (f // 100, f % 100)

ps: dict[int, set[Fig]] = defaultdict(set)
qs: dict[int, set[Fig]] = defaultdict(set)

for s in ss:
    n = 1
    while True:
        f = figurate(n, s)
        
        if f < 1000:
            n += 1
            continue
        if f >= 10000:
            break

        # add to set of figurates
        fs[s].add(f)
        
        # add to prefix/suffix maps
        p,q = pq(f)

        fig = (f, s)
        ps[p].add(fig)
        qs[q].add(fig)

        n += 1

def solve():
    unvisited_nodes = { (f, s) for s in ss for f in fs[s] }

    while unvisited_nodes:
        start_node = unvisited_nodes.pop()
        start_f, start_s = start_node

        queue = [([start_f], { start_s }, True), ([start_f], { start_s }, False)]

        while queue:
            path, path_ss, dir_right = queue.pop()

            f = path[-1 if dir_right else 0]
            p, q = pq(f)

            nbs = ps[q] if dir_right else qs[p]

            for nb in nbs:
                nb_f, nb_s = nb

                if nb_s in path_ss:
                    continue
                
                new_path = path + [nb_f] if dir_right else [nb_f] + path
                new_path_ss = path_ss | { nb_s }

                if len(new_path) < 6:
                    queue.append((new_path, new_path_ss, dir_right))
                else:
                    # check if cyclic
                    p, _ = pq(new_path[0])
                    _, q = pq(new_path[-1])

                    if p == q:
                        print(new_path, sum(new_path))
                        return

if __name__ == '__main__':
    solve()