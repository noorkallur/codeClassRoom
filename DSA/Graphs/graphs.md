# Graphs
[Types of Graphs](https://www.geeksforgeeks.org/graph-types-and-applications/)

Below is a curated list of LeetCode graph problems arranged roughly by difficulty and thematic area. Working through these will help you solidify basic graph traversals, cycle detection, connectivity, topological sorting, union‐find, and more advanced concepts.

---

### Basic Graph Traversals & Connectivity

1. **200. Number of Islands**  
   *Concepts:* Grid traversal using DFS/BFS to count connected components.  
   *Why:* Great for practicing basic DFS/BFS on 2D grids.

2. **133. Clone Graph**  
   *Concepts:* Graph traversal (BFS/DFS) and copying graph structure.  
   *Why:* Teaches you how to manage visited nodes and replicate a graph.

3. **841. Keys and Rooms**  
   *Concepts:* DFS/BFS to check connectivity in graphs.  
   *Why:* Focuses on exploring all nodes from a starting point.

---

### Cycle Detection, Topological Sort, and Tree Verification

4. **207. Course Schedule**  
   *Concepts:* Cycle detection using DFS with recursion stack or Kahn’s algorithm for topological sorting.  
   *Why:* Fundamental for understanding how cycles affect ordering in directed graphs.

5. **210. Course Schedule II**  
   *Concepts:* Builds on the above by finding a valid course order (i.e., topological sort).  
   *Why:* Reinforces cycle detection and ordering tasks.

6. **261. Graph Valid Tree**  
   *Concepts:* Check if a given undirected graph is a tree (connected and acyclic) using DFS/BFS or union-find.  
   *Why:* Combines connectivity and cycle detection in undirected graphs.

---

### Union-Find & Cycle Detection in Undirected Graphs

7. **684. Redundant Connection**  
   *Concepts:* Detecting a cycle in an undirected graph using the union-find data structure.  
   *Why:* Excellent introduction to disjoint set (union-find) for cycle detection.

*(Optional Bonus: Look for other union-find related problems, such as malware spread or network connectivity variations.)*

---

### Shortest Paths & Weighted Graphs

8. **743. Network Delay Time**  
   *Concepts:* Compute shortest paths in weighted directed graphs (typically solved with Dijkstra’s algorithm).  
   *Why:* Practice working with edge weights and priority queues.

9. **1091. Shortest Path in Binary Matrix**  
   *Concepts:* BFS on grids to find shortest paths under given movement rules.  
   *Why:* Applies basic BFS in a grid context with additional obstacles.

---

### Topological Order & Advanced Traversals

10. **269. Alien Dictionary**  
    *Concepts:* Build a graph from character relations and use topological sort to determine ordering.  
    *Why:* Mixes graph construction with topological sorting for ordering problems.

11. **310. Minimum Height Trees**  
    *Concepts:* Use a layer-by-layer removal (similar to topological sort) to find tree centers.  
    *Why:* Teaches interesting properties about tree centers and layered graph processing.

12. **797. All Paths From Source to Target**  
    *Concepts:* Use DFS to enumerate all possible paths in a directed acyclic graph.  
    *Why:* Explores backtracking and complete traversal in DAGs.

---

### Advanced Concepts & Special Graph Problems

13. **332. Reconstruct Itinerary**  
    *Concepts:* Graph traversal with lexicographical order and backtracking (often modeled as Eulerian path problems).  
    *Why:* Excellent for mastering non-trivial DFS where order matters.

14. **1192. Critical Connections in a Network**  
    *Concepts:* Tarjan’s algorithm to find bridges (critical connections) in a network.  
    *Why:* An advanced problem focusing on low-link values and sophisticated DFS-based cycle analysis.

15. **The Maze Series (The Maze, The Maze II, etc.)**  
    *Concepts:* Apply BFS/DFS on matrices with additional movement constraints to find possible paths or shortest paths.  
    *Why:* These problems let you practice graph traversal in grid settings with new twists.

---

### How to Approach This List

- **Start Small:** Begin with the basic traversal/connectivity problems to build intuition.
- **Progress to Order & Detection:** Move to cycle detection and topological sort problems once you’re comfortable with traversals.
- **Tackle Advanced Topics:** Finally, challenge yourself with the advanced problems that require more nuanced algorithmic thinking (Tarjan’s algorithm, backtracking with lexicographical constraints, etc.).

Working through these problems will give you a well-rounded understanding of graph concepts and patterns frequently appearing in interviews and competitive programming.

Feel free to ask for more details on any problem or concept—happy coding on your graph journey!