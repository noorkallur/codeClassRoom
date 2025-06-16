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
add_edge(3,7)
add_edge(3,4)
add_edge(7,8)
add_edge(4,8)

# print the graph
for row in range(len(adj_list)):
  print(f"{row} :-> {adj_list[row]}")


# cycle detection starts here  
# DFS in to the vertex
# if the child is present in the DFS stack that means there is a cycle present
def cycleDetector(vertex):
  stk = []
#   rec_stk = set()
  stk.append(vertex)
  visit = set()

  while stk:
    node = stk.pop()
    visit.add(node)
    # rec_stk.add(node)
    for v in adj_list[node]:
        if v in rec_stk:
            return True
        stk.append(v)
        


  
  
  
