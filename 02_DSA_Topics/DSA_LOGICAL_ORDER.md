# DSA Recommended Logical Order (Independent of Physical Folder Names)

This ordering prioritizes conceptual layering and prerequisite minimization. Physical folders retain existing names; use this as the canonical study sequence.

Level legend:
- L1 Beginner
- L2 Early Intermediate
- L3 Intermediate
- L4 Advanced
- L5 Expert / Specialized

| Order | (Current Folder) | Logical Name | Level | Prerequisites | Rationale |
|-------|-------------------|--------------|-------|---------------|-----------|
| 1 | 01_01_Foundations | Foundations | L1 | – | Big-O, recursion mental model, bit ops primer |
| 2 | 02_02_Core_Techniques_Paradigms | Core Techniques & Paradigms | L1 | Foundations | Two-pointer, sliding window, divide & conquer early pattern vocabulary |
| 3 | 03_03_Data_Structures_Linear | Linear Data Structures | L1 | Foundations | Arrays, linked lists, stacks, queues baseline |
| 4 | 08_08_Searching_Algorithms | Searching | L1 | Linear DS | Binary search mastery reinforces complexity intuition |
| 5 | 09_09_Sorting_Algorithms | Sorting | L1 | Searching | Sorting spectrum → algorithmic tradeoffs |
| 6 | 04_04_Data_Structures_Trees_Hierarchical | Trees & Hierarchical Structures | L2 | Linear DS | Introduce trees, BST, heaps before heavy graph work |
| 7 | 10_10_Graph_Algorithms | Core Graph Algorithms | L2 | Trees basics | Traversals, shortest paths, MST, connectivity foundations |
| 8 | 13_13_Greedy_Algorithms | Greedy | L2 | Sorting, Graph basics | Exploit prior cost reasoning & ordering |
| 9 | 12_12_Dynamic_Programming | Dynamic Programming (Core) | L2 | Recursion, Greedy contrast | Classic DP patterns & state reasoning |
| 10 | 15_15_Backtracking_Search_Problems | Backtracking & Search | L2 | Recursion | Systematic search vs pruning |
| 11 | 16_16_Selection_Streaming_Sketching | Selection & Streaming | L3 | Sorting, Greedy | Quickselect + probabilistic frequency approximations |
| 12 | 11_11_Tree_Algorithms_Techniques | Advanced Tree Techniques | L3 | Core Trees, Graph basics | LCA, HLD, rerooting, centroid decomposition |
| 13 | 14_14_String_Algorithms_Pattern_Matching | String Pattern Matching | L3 | Searching | KMP, Z, Rabin-Karp sequencing before indexes |
| 14 | 05_05_Data_Structures_String_Indexes_Automata | String Indexes & Automata | L3 | Pattern Matching | Suffix structures, automata, FM-index |
| 15 | 17_17_Offline_Decomposition_Techniques | Offline & Decomposition | L3 | Trees, Sorting, DSU | Mo's, small-to-large, coordinate compression |
| 16 | 07_07_Data_Structures_Specialized_Probabilistic | Specialized & Probabilistic DS | L3 | Hashing basics | Bloom, Skip Lists, filters |
| 17 | 21_21_Probabilistic_Randomized_Algorithms | Randomized Algorithms | L4 | Probabilistic DS | Monte Carlo vs Las Vegas, randomized structures |
| 18 | 20_20_Number_Theory_Combinatorics | Number Theory & Combinatorics | L4 | Foundations | Modular arithmetic, primality, combinatorics |
| 19 | 19_19_Computational_Geometry | Computational Geometry | L4 | Sorting, Selection | Geometric primitives, sweepline |
| 20 | 18_18_Game_Theory | Game Theory | L4 | DP, Graph basics | Minimax, alpha-beta builds on recursion & DP |
| 21 | 22_22_Parallel_External-Memory_Big_Data | Parallel & External-Memory | L5 | Core Graph + DS + Performance | Scaling paradigms |
| 22 | 06_06_Data_Structures_Graph_Connectivity | Graph Connectivity (Advanced Structures) | L5 | Core Graph Algorithms | Union-Find variants, dynamic connectivity, planarity, flows extensions |

## Topic Bundling Guidance
Some physical folders (e.g., Trees) cover both introductory and advanced material. When first passing through, focus only on: basic trees, BST, heap, prefix trees. Return later for persistent / segment tree variants.

## Optional Metadata Block Per README
```
---
LogicalOrder: 14
Level: L3
Prerequisites: Pattern Matching
---
```

## Why Connectivity Last?
Dynamic connectivity, advanced flow variations, and planarity often require mastery of several earlier paradigms (DSU, BFS/DFS depth, tree flattening, heavy-light decomposition) making it a capstone cluster.
