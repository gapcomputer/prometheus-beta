from typing import List, Dict, Optional
from collections import deque

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): A graph represented as an adjacency list 
            where graph[u][v] represents the capacity from node u to node v.
        source (int): The source node.
        sink (int): The sink node.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are invalid.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph that will be modified during the algorithm
    residual_graph = {u: graph[u].copy() for u in graph}
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Track parent nodes to reconstruct augmenting path
        parent = {node: None for node in graph}
        
        # Use BFS to find an augmenting path
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            # Check neighbors 
            for neighbor, capacity in residual_graph[current].items():
                # If there's remaining capacity and neighbor not yet visited
                if capacity > 0 and parent[neighbor] is None and neighbor != source:
                    parent[neighbor] = current
                    
                    # If we've found the sink, we can augment flow
                    if neighbor == sink:
                        break
                    
                    queue.append(neighbor)
        
        # If no path to sink was found, we're done
        if parent[sink] is None:
            break
        
        # Find the minimum flow along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual_graph[prev][current])
            current = prev
        
        # Augment flow
        current = sink
        while current != source:
            prev = parent[current]
            residual_graph[prev][current] -= path_flow
            
            # Add reverse edge if it doesn't exist
            if prev not in residual_graph[current]:
                residual_graph[current][prev] = 0
            residual_graph[current][prev] += path_flow
            
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow