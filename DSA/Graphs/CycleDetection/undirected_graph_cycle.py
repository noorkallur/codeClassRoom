# use the same image graph_1.png

# undirected graph
# using graph_1.png as ref
from collections import deque
# add an edge to the graph
def add_edge(n1, n2):
  adj_list[n1].append(n2)
  adj_list[n2].append(n1)


# verticies = 10
# adj_list = [[] for _ in range(verticies)]
# add_edge(1,2)
# add_edge(2,5)
# add_edge(5,7)
# add_edge(3,6)
# add_edge(6,7)
# # add_edge(6,2)
# # add_edge(3,4)
# add_edge(4,8)
# add_edge(8,9)
# add_edge(7,9) # False

# verticies = 6
# adj_list = [[] for _ in range(verticies)]
# # Adding edges to form the cycle
# add_edge(0, 1) 
# add_edge(1, 2) 
# add_edge(2, 3) 
# add_edge(3, 4) 
# add_edge(4, 5) 
# add_edge(5, 0) # True

# verticies = 4
# adj_list = [[] for _ in range(verticies)]
# add_edge(0, 1)
# add_edge(0, 3)
# add_edge(0, 1)
# add_edge(3, 2) # True


verticies = 5
adj_list = [[] for _ in range(verticies)]
add_edge(1,2)
add_edge(1,4) # false


# # self loop, not covered
# verticies = 2
# adj_list = [[] for _ in range(verticies)]
# add_edge(1,1)

# print the graph
for row in range(len(adj_list)):
  print(f"{row} :-> {adj_list[row]}")



# cycle detection code here
# BFS
def detect_cycle():

    def bfs(vertex):
        q = deque()
        q.append(vertex)
        while q:
            node = q.popleft()
            for n in adj_list[node]:
                if n in visited:
                    continue
                if n in q:
                    return True
    
                visited.add(node)
                q.append(n)

        return False
  
    visited = set()
    for v in range(verticies):
        if v not in visited:
            if bfs(v):
                return True

    return False 
  
print(detect_cycle())


# Traditional and Robust way to detect cycle in a graph

def detect_cycle():

    def bfs(vertex):
        q = deque()
        q.append((vertex, -1))
        visited.add(vertex)

        while q:
            node, parent = q.popleft()

            for n in adj_list[node]:
                if n not in visited :
                    q.append((n, node))
                    visited.add(n)

                #n is in visted list, make sure its not the parent
                elif n != parent:
                    #found n which is already visited, i.e. cycle present
                    return True
        # we went throu every node, meaning no loop present
        return False
    
    
    visited = set()
    #if there are diff components, we might want to iterate through all
    for i in range(verticies):
        if i not in visited and bfs(i):
            return True
    
    return False 
                
                



        

  