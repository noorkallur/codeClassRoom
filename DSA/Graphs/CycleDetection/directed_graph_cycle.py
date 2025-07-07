# use the same image graph_1.png

# directed graph
# using graph_1.png as ref
from collections import deque
# add an edge to the graph
def add_edge(n1, n2):
  adj_list[n1].append(n2)

verticies = 9
adj_list = [[] for _ in range(verticies)]

# adding edge
add_edge(1,2)
add_edge(1,3)
add_edge(2,5)
add_edge(2,6)
add_edge(3,4)
add_edge(4,8)
add_edge(8,7)
add_edge(7,3)

# print the graph
for row in range(len(adj_list)):
  print(f"{row} :-> {adj_list[row]}")


# cycle detection starts here  
# DFS-Based Cycle Detection
# Process:
# Perform a Depth-First Search (DFS) from each unvisited vertex.
# Maintain:
# A visited array to mark explored vertices.
# A recursion stack to track the current path.

# Cycle Check:
# If you re-encounter a vertex that is already in the recursion stack, a cycle has been detected.

# Time Complexity: O(V + E)

def cycleDetector():

	def dfs(node):
		visted.add(node)
		rec_stack.add(node)
		for n in adj_list[node]:
			if n not in visted:
				if dfs(n):
					return True
			elif n in rec_stack:
				return True
			
		rec_stack.remove(node)
		return False

	visted = set()
	rec_stack = set()
	for i in range(verticies):
		if dfs(i):
			return True
		
	return False


print(cycleDetector())
  
  
