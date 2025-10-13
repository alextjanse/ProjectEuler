from lib.primes import is_prime, get_primes
from itertools import combinations
from lib.graphs import Graph

def solve() -> None:
    prime_graph = Graph()

    for p in get_primes():
        print("Checking prime", p)

        prime_graph.add_node(p)
        for q in prime_graph.nodes():
            if p == q:
                continue
            pq = int(str(p) + str(q))
            qp = int(str(q) + str(p))
            if is_prime(pq) and is_prime(qp):
                prime_graph.add_edge(p, q)
        
        neighbors = prime_graph.neighbors(p)
        # print("Neighbors:", neighbors)
        if len(neighbors) >= 4:
            for comb in combinations(neighbors, 4):
                if prime_graph.is_clique(comb):
                    print(comb, p, sum(comb) + p)
                    return

if __name__ == '__main__':
    solve()