# Algorithms Index

Comprehensive catalog of algorithmic techniques and paradigms, organized by computational strategy.

## Quick Navigation

### 1. Foundations (`01_Foundations/`)
Mathematical and analytical bedrock for all algorithms.

- **01_Complexity_Analysis** - Big-O, Theta, Omega notation, asymptotic analysis, recurrence relations
- **02_Mathematical_Foundations** - Two-pointer, sliding window, divide & conquer patterns, bit manipulation primer

**Study Order**: Complexity Analysis → Core Techniques  
**Prerequisites**: None (entry point)  
**Level**: L1 (Beginner)

---

### 2. Searching (`02_Searching/`)
Efficient data retrieval strategies.

- **01_Linear_Search** - Sequential scanning, O(n) baseline
- **02_Binary_Search** - Divide & conquer on sorted data, O(log n), variations (lower/upper bound, rotated arrays)

**Study Order**: Linear → Binary Search  
**Prerequisites**: Arrays, complexity fundamentals  
**Level**: L1 (Beginner)

---

### 3. Sorting - Basic (`03_Sorting_Basic/`)
Foundational sorting algorithms for understanding tradeoffs.

- **01_Bubble_Sort** - O(n²), in-place, stable, pedagogical value
- **02_Selection_Sort** - O(n²), in-place, unstable, minimal swaps
- **03_Insertion_Sort** - O(n²), in-place, stable, efficient for small/nearly sorted

**Study Order**: Any order (conceptual foundation)  
**Prerequisites**: Arrays, basic loops  
**Level**: L1 (Beginner)

---

### 4. Sorting - Efficient (`04_Sorting_Efficient/`)
Production-grade sorting with optimal complexity.

- **01_Merge_Sort** - O(n log n) guaranteed, stable, divide & conquer, requires O(n) space
- **02_Quick_Sort** - O(n log n) average, in-place, unstable, cache-friendly
- **03_Heap_Sort** - O(n log n) guaranteed, in-place, unstable, uses heap structure

**Study Order**: Merge → Quick → Heap  
**Prerequisites**: Recursion, basic sorting, heaps (for Heap Sort)  
**Level**: L2 (Early Intermediate)

---

### 5. Divide & Conquer (`05_Divide_Conquer/`)
Problem decomposition into smaller subproblems.

- **01_Principles** - Master theorem, recurrence solving, paradigm overview
- **02_Applications** - Closest pair, Strassen matrix multiplication, Karatsuba

**Study Order**: Principles → Applications  
**Prerequisites**: Recursion, merge/quick sort examples  
**Level**: L2 (Early Intermediate)

---

### 6. Dynamic Programming (`06_Dynamic_Programming/`)
Optimization via overlapping subproblems and memoization.

- **01_Basic_DP** - Fibonacci, knapsack, LCS, LIS, coin change, tabulation vs memoization
- **02_Advanced_DP** - State compression, DP on trees, bitmask DP, digit DP

**Study Order**: Basic DP → Advanced DP  
**Prerequisites**: Recursion, greedy contrast  
**Level**: L2-L3 (Intermediate)

---

### 7. Greedy Algorithms (`07_Greedy/`)
Locally optimal choices leading to global optimum.

- **01_Principles** - Greedy-choice property, optimal substructure, proof techniques
- **02_Applications** - Activity selection, Huffman coding, MST (Prim/Kruskal), Dijkstra

**Study Order**: Principles → Applications  
**Prerequisites**: Sorting, graph basics  
**Level**: L2 (Early Intermediate)

---

### 8. Backtracking (`08_Backtracking/`)
Systematic search with pruning.

- **01_Concepts** - State space trees, pruning strategies, branch & bound
- **02_Problems** - N-Queens, Sudoku solver, subset sum, permutations/combinations

**Study Order**: Concepts → Problems  
**Prerequisites**: Recursion depth, stacks  
**Level**: L2 (Early Intermediate)

---

### 9. Graph Algorithms (`09_Graph_Algorithms/`)
Network traversal, connectivity, and optimization.

- **01_Traversal** - BFS, DFS, topological sort, cycle detection
- **02_Shortest_Path** - Dijkstra, Bellman-Ford, Floyd-Warshall, A*
- **03_Minimum_Spanning_Tree** - Kruskal (DSU), Prim (heaps)
- **04_Advanced** - Network flow (Ford-Fulkerson, Dinic), bipartite matching, strongly connected components (Tarjan/Kosaraju)

**Study Order**: Traversal → Shortest Path → MST → Advanced  
**Prerequisites**: Graph DS, queues, heaps, DSU (for MST)  
**Level**: L2-L4 (Intermediate to Advanced)

---

### 10. Advanced Topics (`10_Advanced_Topics/`)
Specialized computational domains.

- **01_Network_Flow** - Max flow, min cut, bipartite matching, flow decomposition
- **02_Computational_Geometry** - Convex hull, line sweep, closest pair, Voronoi diagrams

**Study Order**: Network Flow → Computational Geometry  
**Prerequisites**: Graph algorithms, sorting, selection  
**Level**: L4 (Advanced)

---

### 11. Specialized Algorithms (`11_Specialized_Algorithms/`)
Domain-specific techniques.

- **01_Bit_Manipulation** - Bitwise ops, masks, subset enumeration, XOR tricks
- **02_Pattern_Matching** - String algorithms (KMP, Rabin-Karp, Boyer-Moore)

**Study Order**: Bit Manipulation → Pattern Matching  
**Prerequisites**: Bitwise operators, string fundamentals  
**Level**: L3 (Intermediate)

---

### 12. Complexity Classes (`12_Complexity_Classes/`)
Theoretical foundations and practical approximations.

- **01_NP_Problems** - P vs NP, NP-complete, NP-hard, reductions
- **02_Approximation** - Approximation algorithms for hard problems, PTAS, FPTAS

**Study Order**: NP Theory → Approximation Strategies  
**Prerequisites**: Solid algorithm analysis background  
**Level**: L4 (Advanced)

---

### 13. Randomized & Parallel (`13_Randomized_Parallel/`)
Probabilistic and concurrent paradigms.

- **01_Randomized_Algorithms** - Monte Carlo, Las Vegas, randomized quickselect, hashing
- **02_Parallel_Algorithms** - PRAM models, parallel prefix, map-reduce patterns

**Study Order**: Randomized → Parallel  
**Prerequisites**: Probability basics, algorithm analysis  
**Level**: L4-L5 (Advanced to Expert)

---

## Recommended Learning Path

```
Foundation (L1):
Complexity Analysis → Searching → Basic Sorting → Efficient Sorting

Core Techniques (L2):
Greedy → Dynamic Programming → Backtracking → Graph Traversal

Advanced (L3-L4):
Graph Advanced → DP Advanced → Computational Geometry → NP Theory

Expert (L5):
Randomized Algorithms → Parallel Algorithms → Network Flow Variants
```

## Cross-References

- **Data Structures**: See `../Data_Structures/INDEX.md` for structure implementations these algorithms require
- **Logical Study Order**: Full dependency graph in root `DSA_LOGICAL_ORDER.md`
- **Complexity Tables**: Each README includes time/space complexity summaries

## Folder Convention

Each subfolder follows `<number>_<Name>` pattern and should contain:
- `README.md` - Algorithm description, pseudocode, complexity, use cases
- `examples.py` or language-specific implementation
- `exercises.md` (optional) - Practice problems with hints

## Status Legend

Within each README:
- ✅ Complete - Fully documented with runnable examples
- 🚧 In Progress - Partial documentation
- 📝 Planned - Outlined, not yet implemented

---

Last Updated: December 2025  
For questions or contributions, refer to repository conventions in `copilot-instructions.md`.
