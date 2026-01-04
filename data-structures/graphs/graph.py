"""
Graph Implementation using Adjacency List
A collection of nodes connected by edges.
"""

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        self.graph[vertex1].append(vertex2)
        if not self.directed:
            self.graph[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if not self.directed and vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]
    
    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])
    
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([v for v in self.graph.get(vertex, []) if v not in visited])
        
        return result
    
    def dfs(self, start_vertex):
        visited = set()
        result = []
        self._dfs_recursive(start_vertex, visited, result)
        return result
    
    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)
    
    def __str__(self):
        return str(self.graph)
