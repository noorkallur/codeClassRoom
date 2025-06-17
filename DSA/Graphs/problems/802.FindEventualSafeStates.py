# three-color DFS technique
# Color Definitions:
# 0 (Unvisited): The node hasn't been processed yet.
# 1 (Visiting): The node is currently in the recursion stack (i.e., being processed).
# 2 (Safe/Processed): The node and its descendants have been fully processed with no cycles detected.

# DFS Process:
# Start: For an unvisited node (color 0), begin DFS by marking it as visiting (color 1).
# Exploration: Recursively explore all adjacent nodes (neighbors).
# If a neighbor is marked as visiting (color 1), a cycle is detected.
# If a neighbor is already safe (color 2), skip further processing as it’s already verified.

# Completion: After processing all neighbors without detecting a cycle, mark the current node as safe (color 2).

# Memoization: Future DFS calls on a safe node (color 2) return immediately, caching the result and avoiding redundant work.

# Backtracking:
# The recursion stack implicitly “backtracks” when a DFS call returns.
# Nodes remain marked (color 1 or color 2) beyond the call, effectively memorizing their status.

def eventualSafeNodes(graph):
    # colors
    # 0->unvisited, 1->visiting, 2->safe
    def dfs(node):
        # return safe if only node is safe, safe -> no cycle detected
        if colors[node] != 0:
            # we have already visited the node, check if its safe or not
            if colors[node] == 2:
                # safe
                return True
            else:
                # 1 is unsafe, as we might have returned from before
                return False
            
        colors[node] = 1
        for neigh in graph[node]:
            if colors[neigh] == 1 or dfs(neigh) == False:
                return False
        colors[node] = 2
        return True


    n = len(graph)
    colors = [0] * n
    output = []
    for i in range(n):
        if dfs(i) == True:
            output.append(i)

    return output
