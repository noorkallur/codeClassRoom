# since its undirected there is no topo order
# since its unit weight we can start relaxing the edges from source/head node
from collections import deque
def shortest_path_unit_undirected(graph, source):
    INF = float('inf')
    vertices = len(graph)
    distances = [INF] * vertices
    distances[source] = 0
    q = deque()
    q.append(source)
    while q:
        node = q.popleft()
        for neigh in graph[node]:
            if distances[neigh] == INF:
                distances[neigh] = distances[node] + 1
                q.append(neigh)

    return distances

# Example usage:
# Adjacency list for undirected graph with 5 nodes (0-4)
graph = [
    [1, 2],    # 0 is connected to 1 and 2
    [0, 3],    # 1 is connected to 0 and 3
    [0, 3],    # 2 is connected to 0 and 3
    [1, 2, 4], # 3 is connected to 1, 2, and 4
    [3]        # 4 is connected to 3
]

print(shortest_path_unit_undirected(graph, 0))  # Output: [0, 1, 1, 2, 3]