# In a graph, if there's a one-way connection from A to B (meaning A must happen before B), 
# a topological sort makes sure A is placed before B in the order.
# This ordering is only possible when there are no circular dependencies.
# watch the video only for visual representation https://www.youtube.com/watch?v=eL-

# top sorts are not unique, there could be multiple answers

#DFS based top sort
# this is for a DAG, if cycles present this will break
def topSort(graph):
    def dfs(node):
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                dfs(neigh)
        top_stack.append(node)

    visited = set()
    top_stack = []
    n = len(graph)
    for i in range(n):
        if i not in visited:
            dfs(i)
    return top_stack[::-1]

# Example index-based graph adjaceny list
# graph = [
#     [1, 2],
#     [3],
#     [3],
#     []
# ]

# print("Topological Sort:", topSort(graph))

# what if cycles are present

def topSort_cycle(graph):
    # colors
    # 0->unvisited, 1->visiting, 2->safe
    def dfs(node):
        if colors[node] != 0:
            return colors[node] == 2
        
        colors[node] = 1
        for neigh in graph[node]:
            if colors[neigh] == 1 or dfs(neigh) == False:
                return False
        colors[node] = 2
        top_stk.append(node)
        return True

    n = len(graph)
    colors = [0] * n
    top_stk = []
    for i in range(n):
        if colors[i] == 0:
            dfs(i)

    return top_stk[::-1]


# Example index-based graph adjaceny list
graph = [
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
# graph = [
#     [1],      # Node 0 points to Node 1
#     [2],      # Node 1 points to Node 2
#     [0, 3],   # Node 2 points back to Node 0 (cycle) and to Node 3 (acyclic)
#     [4],      # Node 3 points to Node 4
#     []        # Node 4 is a sink in the acyclic subgraph
# ]
print("Topological Sort:", topSort_cycle(graph))

def topSort_cycle(graph):
    # colors
    # 0->unvisited, 1->visiting, 2->safe
    def dfs(node):
        if colors[node] != 0:
            return colors[node] == 2
        
        colors[node] = 1
        for neigh in graph[node]:
            if colors[neigh] == 1 or dfs(neigh) == False:
                return False
        colors[node] = 2
        top_stk.append(node)
        return True

    n = len(graph)
    colors = [0] * n
    top_stk = []
    for i in range(n):
        if colors[i] == 0:
            if not dfs(i):
                return []

    return top_stk[::-1]