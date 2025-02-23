from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure for tracking connected components.
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with given number of vertices.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Union of two sets with union by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (sets were different), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def boruvka_mst(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    :param n: Number of vertices
    :param edges: List of edges with (start, end, weight)
    :return: List of edges in the minimum spanning tree
    :raises ValueError: If graph is not connected or edges is empty
    """
    # Validate input
    if not edges:
        raise ValueError("No edges provided")
    
    # Sort edges by weight to help with initial processing
    edges.sort(key=lambda x: x[2])
    
    # Initialize disjoint set
    ds = DisjointSet(n)
    
    # MST to store the result
    mst = []
    
    # Number of components
    components = n
    
    while components > 1:
        # Track cheapest edge for each component
        cheapest = [None] * n
        
        # Find cheapest edge for each component
        for u, v, w in edges:
            set_u = ds.find(u)
            set_v = ds.find(v)
            
            # Skip if same component
            if set_u == set_v:
                continue
            
            # Update cheapest edge if needed
            if cheapest[set_u] is None or w < cheapest[set_u][2]:
                cheapest[set_u] = (u, v, w)
            
            if cheapest[set_v] is None or w < cheapest[set_v][2]:
                cheapest[set_v] = (u, v, w)
        
        # Add cheapest edges to MST
        for cheap_edge in cheapest:
            if cheap_edge is None:
                continue
            
            u, v, w = cheap_edge
            
            # If not in same set, add to MST and merge
            if ds.union(u, v):
                mst.append(cheap_edge)
                components -= 1
        
        # Break if no more edges can be added
        if len(mst) == n - 1:
            break
    
    # Check if graph is fully connected
    if components > 1:
        raise ValueError("Graph is not connected")
    
    return mst