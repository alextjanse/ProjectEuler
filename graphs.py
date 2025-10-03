'''Graphs module'''

class Graph:
    '''Graph class, with different functions for graph calculations.'''
    
    def __init__(self):
        self.V = set()
        self.E = set()
    
    def addVertex(self, v):
        if v in self.V:
            raise ValueError("Vertex already exists in the graph.")
        self.V.add(v)
    
    def addEdge(self, u, v):
        if (u > v):
            u, v = v, u
        if u not in self.V or v not in self.V:
            raise ValueError("Both vertices must be in the graph.")
        if (u == v):
            raise ValueError("No self loops allowed.")
        if (u, v) in self.E:
            raise ValueError("Edge already exists in the graph.")
        self.E.add((u, v))

    def getDegree(self, v):
        if v not in self.V:
            raise ValueError("Vertex must be in the graph.")
        degree = 0
        for u, w in self.E:
            if u == v or w == v:
                degree += 1
        return degree
    
    def getNeighbors(self, v):
        if v not in self.V:
            raise ValueError("Vertex must be in the graph.")
        return [u if w == v else w for u, w in self.E if u == v or w == v]

    def removeVertex(self, v):
        if v not in self.V:
            raise ValueError("Vertex must be in the graph.")
        self.V.remove(v)
        self.E = [(u, w) for u, w in self.E if u != v and w != v]
    
    def removeEdge(self, u, v):
        if (u > v):
            u, v = v, u
        if (u, v) not in self.E:
            raise ValueError("Edge must be in the graph.")
        self.E.remove((u, v))
    
    def getSubgraph(self, vertices):
        subgraph = Graph()
        for v in vertices:
            if v not in self.V:
                raise ValueError("All vertices must be in the graph.")
            subgraph.addVertex(v)
        for u, v in self.E:
            if u in vertices and v in vertices:
                subgraph.addEdge(u, v)
        return subgraph
    
    def isClique(self, vertices):
        for vi in vertices:
            for vj in vertices:
                if vi == vj:
                    continue
                if (vi, vj) not in self.E and (vj, vi) not in self.E:
                    return False
        return True

    def __str__(self):
        return f"G=(V={self.V}, E={self.E})"