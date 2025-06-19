# this is also called KAHNS algorithm
# The graph should be a DAG
# A DAG will have one node indegree 0 and also node with outdegree 0

# HOW to perform top sort
# step 1: find indegree of all the vertices
# step 2: push all nodes with indegree 0 to the BFS queue
# Refer image toplogical_sort_bfs_1.png
from collections import deque
from typing import List

def topSort(adj_list: List[List[int]]) -> List[int]:
    """
    Return a topological ordering of a DAG in O(V+E), or [] if a cycle exists.
    """

    n = len(adj_list)

    # 1. Compute in-degree of each node
    indegree_list = [0] * n
    for vertex in range(n):
        for neigh in adj_list[vertex]:
            indegree_list[neigh] +=1
    
    print(indegree_list)

    # 2. Initialize queue with all nodes of in-degree zero
    q = deque()
    for i in range(n):
        if indegree_list[i] == 0:
            q.append(i)

    topo_order = []

    # 3. Process nodes in queue
    while q:
        vertex = q.popleft()
        topo_order.append(vertex)
        # decrease the degrees of the impacted verticies
        for neigh in adj_list[vertex]:
            indegree_list[neigh] -=1
            if indegree_list[neigh] == 0:
                q.append(neigh)

    # 4. If we’ve output all nodes, return the order; else a cycle exists
    if len(topo_order) == n:
        return topo_order
    else:
        # cycle found in graph
        return []

adj_list = [
    [1, 2],
    [3],
    [3],
    []
]
adj_list = [
    [],
    [],
    [1],
    [0, 2],
    [0, 1],
    [0, 3]
]
adj_list = [
    [1, 2],
    [3],
    [3],
    []
]
graph_with_cycle = [
    [1],  # Node 0 points to Node 1
    [2],  # Node 1 points to Node 2
    [0]   # Node 2 points back to Node 0, forming a cycle 0 -> 1 -> 2 -> 0
]
graph_with_cycle = [
    [1],      # Node 0 points to Node 1
    [2],      # Node 1 points to Node 2
    [1, 3],   # Node 2 points back to Node 0 (cycle) and to Node 3 (acyclic)
    [4],      # Node 3 points to Node 4
    []        # Node 4 is a sink in the acyclic subgraph
]
print(topSort(graph_with_cycle))