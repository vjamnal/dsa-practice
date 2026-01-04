# problem: Invert Binary Tree
# approach: Recursive DFS
# time: O(n)
# space: O(h) where h is height

"""
Invert Binary Tree
Mirror a binary tree (swap left and right children).

LeetCode #226
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """
    Recursive solution - O(n) time, O(h) space where h is height
    """
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def invert_tree_iterative(root):
    """
    Iterative solution using queue (BFS) - O(n) time, O(n) space
    """
    if not root:
        return None
    
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


def print_tree_inorder(root):
    """Helper function to print tree inorder."""
    if not root:
        return []
    return print_tree_inorder(root.left) + [root.val] + print_tree_inorder(root.right)


if __name__ == "__main__":
    print("Invert Binary Tree Tests:")
    # Tree: 4, 2, 7, 1, 3, 6, 9
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    print(f"Original: {print_tree_inorder(root)}")
    inverted = invert_tree(root)
    print(f"Inverted: {print_tree_inorder(inverted)}")
