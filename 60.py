from primes import getPrimes, isPrime
from itertools import combinations
from collections import defaultdict
from graphs import Graph

if __name__ == '__main__':
    primes = getPrimes(10 ** 7)
    prime_graph = Graph()

    for p in primes:
        print("Checking prime", p)
        prime_graph.addVertex(p)
        neighbors = []
        for q in prime_graph.V:
            if p == q:
                continue
            pq = str(p) + str(q)
            qp = str(q) + str(p)
            if isPrime(int(pq)) and isPrime(int(qp)):
                prime_graph.addEdge(p, q)
                neighbors.append(q)
        
        print("Neighbors:", neighbors)
        if len(neighbors) < 4:
            continue
        for comb in combinations(neighbors, 4):
            if prime_graph.isClique(comb):
                print(comb, sum(comb) + p)
                exit(0)
