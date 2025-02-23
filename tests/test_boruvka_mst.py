import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Initial state
    assert ds.find(0) != ds.find(1)
    
    # Union and find
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Multiple unions
    ds.union(2, 3)
    ds.union(1, 3)
    assert ds.find(0) == ds.find(2)
    assert ds.find(1) == ds.find(3)

def test_boruvka_simple_graph():
    """Test Boruvka's algorithm on a simple connected graph."""
    n = 4
    edges = [
        (0, 1, 1),   # Edge 1
        (0, 2, 4),   # Edge 2
        (1, 2, 2),   # Edge 3
        (1, 3, 3),   # Edge 4
        (2, 3, 5)    # Edge 5
    ]
    
    mst = boruvka_mst(n, edges)
    
    # Check MST properties
    assert len(mst) == 3  # n-1 edges
    assert set(mst) == {(0, 1, 1), (1, 2, 2), (1, 3, 3)}

def test_boruvka_disconnected_graph():
    """Test Boruvka's algorithm with an unconnected graph."""
    n = 4
    edges = [
        (0, 1, 1),
        (2, 3, 2)
    ]
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        boruvka_mst(n, edges)

def test_boruvka_empty_edges():
    """Test Boruvka's algorithm with no edges."""
    n = 3
    edges = []
    
    with pytest.raises(ValueError, match="No edges provided"):
        boruvka_mst(n, edges)

def test_boruvka_complex_graph():
    """Test Boruvka's algorithm on a more complex graph."""
    n = 6
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 6),
        (3, 4, 7),
        (3, 5, 2),
        (4, 5, 4)
    ]
    
    mst = boruvka_mst(n, edges)
    
    # Check MST properties
    assert len(mst) == 5  # n-1 edges
    
    # Validate total weight is minimal
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 12  # Minimal spanning tree weight

def test_edge_sorting():
    """Ensure algorithm works regardless of input edge order."""
    n = 4
    # Deliberately shuffle edges
    edges = [
        (1, 2, 2),   # Middle weight
        (0, 1, 1),   # Lowest weight
        (1, 3, 3),   # Highest weight
        (0, 2, 4),
        (2, 3, 5)
    ]
    
    mst = boruvka_mst(n, edges)
    
    # Check MST is consistent
    assert len(mst) == 3
    assert set(mst) == {(0, 1, 1), (1, 2, 2), (1, 3, 3)}