# Data Structures Index

Comprehensive catalog of data structure implementations, organized by fundamental categories.

## Quick Navigation

### 1. Linear Data Structures (`01_Linear_DS/`)
Sequential data organization with constant or linear access patterns.

- **01_Arrays** - Contiguous memory, O(1) access, fixed/dynamic sizing
- **02_Linked_Lists** - Node-based, dynamic allocation, various link patterns (single, double, circular)
- **03_Stacks** - LIFO principle, function calls, expression evaluation, backtracking foundations
- **04_Queues** - FIFO principle, BFS, scheduling, circular & priority variants

**Study Order**: Arrays → Stacks → Queues → Linked Lists  
**Prerequisites**: Basic complexity analysis (Big-O)  
**Level**: L1 (Beginner)

---

### 2. Non-Linear Data Structures (`02_NonLinear_DS/`)
Hierarchical and network-based organization for complex relationships.

- **01_Trees** - Binary trees, BST, AVL, Red-Black, B-trees, Segment trees
- **02_Graphs** - Adjacency matrix/list, directed/undirected, weighted, connectivity
- **03_Heaps** - Min/max heaps, priority queues, heap sort, Fibonacci heaps
- **04_Hash_Tables** - Hash functions, collision resolution (chaining, open addressing), load factors

**Study Order**: Trees (basic BST) → Heaps → Hash Tables → Graphs → Advanced Trees  
**Prerequisites**: Linear DS, recursion fundamentals  
**Level**: L2 (Early Intermediate)

---

### 3. String Data Structures (`03_String_DS/`)
Specialized structures for text processing and pattern matching.

- **01_String_Algorithms** - KMP, Rabin-Karp, Boyer-Moore, Z-algorithm pattern matching
- **02_Tries** - Prefix trees, suffix arrays, suffix trees, FM-index, Aho-Corasick automata

**Study Order**: String Algorithms (pattern matching) → Tries → Advanced String Indexes  
**Prerequisites**: Arrays, basic searching algorithms  
**Level**: L3 (Intermediate)

---

### 4. Specialized Data Structures (`04_Specialized_DS/`)
Advanced structures for specific problem domains.

- **01_Disjoint_Sets** - Union-Find, DSU with path compression & union by rank, dynamic connectivity
- **02_Advanced_Trees** - Persistent data structures, Bloom filters, Skip lists, probabilistic structures

**Study Order**: Disjoint Sets → Probabilistic Structures  
**Prerequisites**: Trees, Graphs, Hashing fundamentals  
**Level**: L3-L4 (Intermediate to Advanced)

---

## Learning Progression

```
Beginner Path (L1):
Arrays → Stacks → Queues → Linked Lists → Basic Trees → Basic Heaps

Intermediate Path (L2-L3):
BST → Hash Tables → Graphs → String Algorithms → Tries → Disjoint Sets

Advanced Path (L4+):
Segment Trees → Suffix Structures → Persistent DS → Probabilistic DS
```

## Cross-References

- **Algorithms**: See `../Algorithms/INDEX.md` for algorithmic techniques that leverage these structures
- **Logical Study Order**: Consult `DSA_LOGICAL_ORDER.md` in root for prerequisite chains
- **Performance**: Most READMEs include time/space complexity tables

## Folder Convention

Each subfolder follows `<number>_<Name>` pattern and should contain:
- `README.md` - Concepts, complexity, use cases, visualizations
- `examples.py` or language-specific implementation
- `exercises.md` (optional) - Practice problems

## Status Legend

Within each README, you may find:
- ✅ Complete - Fully documented with examples
- 🚧 In Progress - Partial implementation
- 📝 Planned - Outlined, not yet coded

---

Last Updated: December 2025  
For questions or contributions, refer to repository conventions in `copilot-instructions.md`.
