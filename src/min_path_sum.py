class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    """
    Find the minimum path sum from root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        int: The minimum path sum, or float('inf') if the tree is empty
    """
    # Handle empty tree case
    if not root:
        return float('inf')
    
    # Leaf node case
    if not root.left and not root.right:
        return root.val
    
    # Recursive calculation of minimum path sum
    left_min = float('inf')
    right_min = float('inf')
    
    # Recursively find minimum path sum for left subtree
    if root.left:
        left_min = min_path_sum(root.left) + root.val
    
    # Recursively find minimum path sum for right subtree  
    if root.right:
        right_min = min_path_sum(root.right) + root.val
    
    # Return the minimum of left and right paths
    return min(left_min, right_min)