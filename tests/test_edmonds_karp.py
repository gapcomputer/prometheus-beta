import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_flow():
    """Test a simple graph with known maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 19

def test_disconnected_graph():
    """Test a graph where there's no path from source to sink."""
    graph = {
        0: {1: 5},
        1: {0: 5},
        2: {3: 10},
        3: {2: 10}
    }
    assert edmonds_karp(graph, 0, 3) == 0

def test_single_edge_graph():
    """Test a graph with just one edge."""
    graph = {
        0: {1: 100},
        1: {}
    }
    assert edmonds_karp(graph, 0, 1) == 100

def test_complex_graph():
    """Test a more complex network flow scenario."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1},
        2: {3: 2, 4: 2},
        3: {5: 2},
        4: {5: 3},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 4

def test_invalid_nodes():
    """Test that ValueError is raised for invalid source or sink."""
    graph = {
        0: {1: 10},
        1: {}
    }
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        edmonds_karp(graph, 2, 1)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        edmonds_karp(graph, 0, 2)

def test_zero_capacity_graph():
    """Test a graph with zero capacities."""
    graph = {
        0: {1: 0, 2: 0},
        1: {2: 0},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 0