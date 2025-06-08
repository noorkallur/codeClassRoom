# undirected graph
# using graph_1.png as ref
from collections import deque
# add an edge to the graph
def add_edge(n1, n2):
  adj_list[n1].append(n2)
  adj_list[n2].append(n1)

verticies = 9
adj_list = [[] for _ in range(verticies)]

# adding edge
add_edge(1,2)
add_edge(1,3)
add_edge(2,5)
add_edge(2,6)
add_edge(3,7)
add_edge(3,4)
add_edge(7,8)
add_edge(4,8)

# print the graph
for row in range(len(adj_list)):
  print(f"{row} :-> {adj_list[row]}")

# DFS for graph
visited = [0] * verticies

def dfs(node):
  if visited[node] == True:
    return
  
  visited[node] = 1
  for v in adj_list[node]:
    dfs(v)

head = 2
dfs(2)
print(visited)

# # what if the graph has disconnected components
# # Loop through all vertices to run DFS on each disconnected component
# for node in range(verticies):
#     if not visited[node]:
#         dfs(node)

# # Finally, print the visited state
# print(visited)

