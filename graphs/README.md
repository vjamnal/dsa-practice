# Graphs

Graph problems including traversal, shortest path, and connectivity.

## Problems

1. **Number of Islands** - Count connected components
2. **Clone Graph** - Deep copy a graph
3. **Course Schedule** - Detect cycle in directed graph
4. **Pacific Atlantic Water Flow** - Matrix traversal problem
5. **Word Ladder** - Shortest transformation sequence

## Graph Representation

```python
# Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

## Common Algorithms

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Dijkstra's Algorithm
- Union Find (Disjoint Set)
- Topological Sort

## Time Complexity

- DFS/BFS: O(V + E) where V is vertices, E is edges
