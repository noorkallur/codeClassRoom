# please use dijkstra_graph.png as reference
# bigger video:
# https://www.youtube.com/watch?v=pSqmAO-m7Lk&t=731s

# the below is LAZY dijkstra with min heap

# Steps:
# Uses a min-heap to pick the current node in O(log V)
# Pushes every new (distance, node) pair, potentially creating duplicates
# Skips stale heap entries by comparing popped distance against dist[node]
# Runs in O((V + E) log V) for sparse graphs, but introduces heap-management overhead

import heapq
def dijkstra(graph, source):
    INF = float('inf')
    dist = {v: INF for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    # heap with source and 0 distance
    hp = [(0, source)]
    
    while hp:
        d, node = heapq.heappop(hp)
        # skip multiple entries in heap, if better dist is found
        if d > dist[node]:
            continue

        for neigh, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neigh]:
                dist[neigh] = new_dist
                prev[neigh] = node
                heapq.heappush(hp, (new_dist, neigh))
    
    return dist, prev


def reconstruct_path(prev, target):
    path = []
    next = target
    while next:
        path.append(next)
        next = prev[next]

    return path[::-1]


graph = {
    'A': [('B', 2), ('D', 8)],
    'B': [('A', 2), ('D', 5), ('E', 6)],
    'C': [('E', 9), ('F', 3)],
    'D': [('A', 8), ('B', 5), ('E', 3), ('F',2)],
    'E': [('B', 6), ('D', 3), ('F', 1), ('C', 9)],
    'F': [('D', 2), ('F', 1), ('C', 3)]
}


# example 1
source = 'A'
destination = 'C'
dist, prev = dijkstra(graph, source)
print("Distances:", dist)
print(f"Path {source} → {destination} : {reconstruct_path(prev, destination)}")


# example 2
source = 'B'
destination = 'C'
dist, prev = dijkstra(graph, source)
print("Distances:", dist)
print(f"Path {source} → {destination} : {reconstruct_path(prev, destination)}")
