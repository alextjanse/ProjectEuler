from collections.abc import Iterable

'''Graphs module'''

from typing import Hashable, TypeVar, Generic

T = TypeVar('T', bound=Hashable)  # Type alias for graph nodes

class Graph(Generic[T]):
    def __init__(self):
        self.adj: dict[T, set[T]] = {}
    
    def nodes(self) -> set[T] : return set(self.adj.keys())

    def add_node(self, node: T) -> None:
        self.adj.setdefault(node, set())

    def add_edge(self, u: T, v: T) -> None:
        self.add_node(u)
        self.add_node(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def neighbors(self, node: T) -> set[T]:
        return self.adj.get(node, set())
    
    def is_clique(self, nodes: Iterable[T]) -> bool:
        for u in nodes:
            for v in nodes:
                if u != v and v not in self.neighbors(u):
                    return False
        return True
    
class DiGraph(Graph):
    def add_edge(self, u: T, v: T) -> None:
        self.add_node(u)
        self.add_node(v)
        self.adj[u].add(v)

    def predecessors(self, node: T) -> set[T]:
        return {u for u, vs in self.adj.items() if node in vs}
    
    def successors(self, node: T) -> set[T]:
        return self.adj.get(node, set())
    
    def is_acylcic(self) -> bool:
        visited = set()
        rec_stack = set()

        def visit(v: Hashable) -> bool:
            if v in rec_stack:
                return False
            if v in visited:
                return True
            
            visited.add(v)
            rec_stack.add(v)
            for neighbor in self.successors(v):
                if not visit(neighbor):
                    return False
            rec_stack.remove(v)
            return True

        for node in self.nodes():
            if node not in visited:
                if not visit(node):
                    return False
        return True