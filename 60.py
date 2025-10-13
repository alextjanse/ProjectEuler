from primes import sieve, is_prime
from itertools import combinations
from graphs import Graph

def solve() -> None:
    primes = sieve(10 ** 7)
    prime_graph = Graph()

    for p in primes:
        print("Checking prime", p)

        prime_graph.add_node(p)
        neighbors = set()
        for q in prime_graph.nodes():
            if p == q:
                continue
            pq = int(str(p) + str(q))
            qp = int(str(q) + str(p))
            if is_prime(pq) and is_prime(qp):
                prime_graph.add_edge(p, q)
                neighbors.add(q)
        
        # print("Neighbors:", neighbors)
        if len(neighbors) >= 4:    
            for comb in combinations(neighbors, 4):
                if prime_graph.is_clique(comb):
                    print(comb, p, sum(comb) + p)
                    return

if __name__ == '__main__':
    solve()