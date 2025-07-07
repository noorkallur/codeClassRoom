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


# BFS using deque
# taking head at 3
q = deque()
head = 3
q.append(head)
visited = [0] * verticies
visited[head] = 1
while q:
    node = q.popleft()
    print(node)
    #fetch and iterate thr neighbors
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            visited[neighbor] = 1
            q.append(neighbor)
    print(q)

print(visited)


      
      

