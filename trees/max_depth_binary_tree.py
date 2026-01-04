# problem: Maximum Depth of Binary Tree
# approach: Recursive DFS
# time: O(n)
# space: O(h) where h is height

"""
Maximum Depth of Binary Tree
Find the maximum depth (height) of a binary tree.

LeetCode #104
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    Recursive DFS - O(n) time, O(h) space where h is height
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1


def max_depth_iterative(root):
    """
    Iterative BFS using queue - O(n) time, O(n) space
    """
    if not root:
        return 0
    
    queue = [(root, 1)]
    max_level = 0
    
    while queue:
        node, level = queue.pop(0)
        max_level = max(max_level, level)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return max_level


if __name__ == "__main__":
    print("Maximum Depth Tests:")
    # Tree: 3, 9, 20, null, null, 15, 7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Max depth: {max_depth(root)}")  # 3
    print(f"Max depth (iterative): {max_depth_iterative(root)}")  # 3
