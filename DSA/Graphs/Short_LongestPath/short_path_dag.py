# if its a DAG, better use DFS as the topo order is already reversed
# when to use DFS on short path
# • Only on Directed Acyclic Graphs (DAGs) – DFS gives you a topological ordering in O(V+E) time. – Once you have that order, you can relax edges in one pass for shortest paths.
# • When you don’t need a priority queue – DFS + DP (via topo order) runs in linear time, vs. Dijkstra’s O((V+E) log V). – Works even if edge weights are negative (so long as the graph stays acyclic).
# • When you’re okay with one fixed source – You pick your “head” node, run DFS topo sort from all nodes (or just reachable ones), then do the relaxation. – If you need multi-source or dynamic sources, other algorithms might be a better fit.
# • Not for unweighted graphs—that’s BFS’s domain – If weights are all “1,” BFS is simpler and finds shortest paths by nature of level-by-level exploration.
# • Avoid for general graphs or negative cycles – DFS-based topo + relaxation assumes no cycles. – For arbitrary weights with possible cycles, use Bellman-Ford (detects negative cycles) or Dijkstra (if non-negative).
def shortest_path_dag(graph, head):
    """
    Compute shortest paths in a DAG from a given source (head) node.

    graph: dict[int, list[tuple(int, int)]]
        Adjacency list mapping each node to a list of (neighbor, weight) pairs.
    head: int
        The source node from which we calculate shortest distances.
    Returns: list[float]
        List of shortest distances from head to every node (∞ if unreachable).
    """

    # --- Part 1: Compute topological order via DFS postorder ---
    visited = set()      # Track nodes we've already visited in DFS
    topo_order = []      # Will hold nodes in reverse postorder (i.e., a valid topo sort)

    def dfs(u):
        """Recursively visit all descendants of u, then append u to topo_order."""
        visited.add(u)
        for v, _ in graph[u]:
            if v not in visited:
                dfs(v)
        topo_order.append(u)  # All neighbors done, now record u

    # Run DFS from every node to cover disconnected parts of the graph
    for node in graph:
        if node not in visited:
            dfs(node)

    # Now topo_order is reverse topological order; popping from it gives correct order
    # e.g., if topo_order == [3, 1, 0], then popping yields 0→1→3

    # --- Part 2: Initialize distances ---
    n = len(graph)
    INF = float('inf')
    dist = [INF] * n       # dist[i] will hold shortest distance from head to i
    dist[head] = 0         # Distance to the source is zero

    # --- Part 3: Relax edges in topological order ---
    while topo_order:
        u = topo_order.pop()    # Take next node in topological order
        if dist[u] == INF:
            # If u is still ∞, it's not reachable from head → skip relaxation
            continue

        # Try to improve distances to all neighbors of u
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist

    return dist


# --- Example usage ---
if __name__ == "__main__":
    graph = {
        0: [(1, 2), (2, 3)],  # edges 0→1 (w=2), 0→2 (w=3)
        1: [(3, 4)],          # 1→3 (w=4)
        2: [(3, 1)],          # 2→3 (w=1)
        3: [(4, 2)],          # 3→4 (w=2)
        4: []                 # 4 has no outgoing edges
    }
    head = 0
    distances = shortest_path_dag(graph, head)
    print(distances)  # Expected: [0, 2, 3, 4, 6]
    head = 2
    distances = shortest_path_dag(graph, head)
    print(distances)  # Expected: [inf, inf, 0, 1, 3]


# Note:
# Why topo sort
# You need topological order in a DAG for shortest path because it guarantees you always process each node only after all possible ways to reach it have already been considered.
# Without topological order, you might update a node’s distance before you’ve found the best way to get there, leading to wrong answers.

