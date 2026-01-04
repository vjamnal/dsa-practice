# Trees

Tree-based problems including binary trees, BST, and tree traversals.

## Problems

1. **Invert Binary Tree** - Mirror a binary tree
2. **Maximum Depth of Binary Tree** - Find tree height
3. **Validate Binary Search Tree** - Check if tree is valid BST
4. **Lowest Common Ancestor** - Find LCA of two nodes
5. **Binary Tree Level Order Traversal** - Level order traversal

## Tree Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Common Techniques

- Depth-First Search (DFS)
  - Inorder: Left -> Root -> Right
  - Preorder: Root -> Left -> Right
  - Postorder: Left -> Right -> Root
- Breadth-First Search (BFS)
- Recursion

## Time Complexity

- BST operations (balanced): O(log n)
- Tree traversal: O(n)
