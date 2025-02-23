import pytest
from src.min_path_sum import TreeNode, min_path_sum

def test_empty_tree():
    """Test minimum path sum for an empty tree"""
    assert min_path_sum(None) == float('inf')

def test_single_node_tree():
    """Test minimum path sum for a tree with only a root node"""
    root = TreeNode(5)
    assert min_path_sum(root) == 5

def test_simple_tree_with_min_left_path():
    """Test a simple tree where left path is the minimum"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    assert min_path_sum(root) == 15  # 10 + 5

def test_simple_tree_with_min_right_path():
    """Test a simple tree where right path is the minimum"""
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(5)
    assert min_path_sum(root) == 15  # 10 + 5

def test_complex_multi_level_tree():
    """Test a more complex multi-level tree"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(3)
    assert min_path_sum(root) == 19  # 10 + 5 + 2 (leftmost path)

def test_unbalanced_tree():
    """Test an unbalanced tree with varying path lengths"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.right = TreeNode(2)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(3)
    assert min_path_sum(root) == 19  # 10 + 5 + 2 or 10 + 15 + 3