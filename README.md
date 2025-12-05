# Python Programming

A comprehensive Python learning resource covering 42+ major topics from core fundamentals to advanced algorithms, data structures, architecture patterns, and best practices. Perfect for beginners to advanced learners seeking a structured curriculum with hands-on examples and exercises.

[![License](https://img.shields.io/github/license/yasir-arafat123/Python_Programming)](https://github.com/yasir-arafat123/Python_Programming/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/yasir-arafat123/Python_Programming)](https://github.com/yasir-arafat123/Python_Programming/commits)
[![Repo Size](https://img.shields.io/github/repo-size/yasir-arafat123/Python_Programming)](https://github.com/yasir-arafat123/Python_Programming)
[![Open Issues](https://img.shields.io/github/issues/yasir-arafat123/Python_Programming)](https://github.com/yasir-arafat123/Python_Programming/issues)
![Python](https://img.shields.io/badge/python-3.x-blue)

Languages in this repository: Python (94.4%), PowerShell (5.6%).

---

## Table of Contents
- [Overview](#overview)
- [Audience & Goals](#audience--goals)
- [Quick Start Tracks](#quick-start-tracks)
- [Repository Structure](#repository-structure)
  - [01_Python_Core_Topics](#01_python_core_topics)
  - [02_DSA_Topics](#02_dsa_topics)
  - [03_Real_World_Applications](#03_real_world_applications)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [PowerShell Helpers](#powershell-helpers)
- [Tips & Conventions](#tips--conventions)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview
This repository is a comprehensive learning resource and reference for Python programming, covering everything from core fundamentals to advanced data structures and algorithms. It contains:
- **01_Python_Core_Topics**: 20+ major categories covering Python fundamentals, OOP, advanced concepts, architecture, and best practices
- **02_DSA_Topics**: 22+ major categories covering algorithms, data structures, complexity analysis, and computational techniques
- Hands‑on scripts and examples with clear, well‑commented code
- Problem‑solving exercises ranging from beginner to advanced
- A small set of PowerShell helpers for Windows developer workflow

## Audience & Goals
- **Self-taught beginners** who need a structured, Windows-friendly path from “Hello, World” to confident scripting.
- **Professional developers** who want production-grade practices: typing, observability, deployment, architecture, and refactoring.
- **Interview-focused learners** who need a deep, topic-organized DSA library.

By design this is a **curriculum monorepo**, not a single textbook or course. Each folder is self-contained, intentionally small, and meant to be explored alongside the [INDEX](INDEX/README.md), which acts as a roadmap and status board.

## Quick Start Tracks
Choose the lane that matches your starting point. Each bullet links to a folder you can open directly in VS Code.

- **Beginner Python Track** – Start at `A_Python_Core/A.0_Getting_Started/`, then work through folders `1`–`9` for language fundamentals plus tooling basics.
- **Production Python Track** – If you already ship scripts, jump to `A_Python_Core/A.10_Advanced/` through `A.24_Refactoring/` to layer in typing, observability, concurrency, performance, security, docs, and deployment.
- **DSA Interview Track** – Use `B_DSA/DSA_LOGICAL_ORDER.md` as the sequence, dive into the numbered topic folders, and practice with the included exercises.
- **Data Science Track** – Combine the Beginner Track basics with `A_Python_Core/A.21_Data_Science/` plus the NUMPY/Pandas curricula in the repo root.

Each topic folder follows the repo convention: a short `README.md`, runnable `examples.py`, and optional `exercises.md`. The [INDEX](INDEX/README.md) ties it all together and shows progress.

## Repository Structure

### A_Python_Core

A comprehensive curriculum covering Python from basics to advanced topics:

0. **Getting Started** - Install Python, VS Code, create your first virtual environment, run `hello_world.py`
1. **Setup & Packaging** - PIP, Virtual Environments, Modules, Imports, Project Structure
2. **Core Language** - Syntax, Variables, Data Types, Numbers, Operators, Math, User Input/Output
3. **Strings** - String manipulation, Formatting, RegEx, Unicode & Encoding
4. **Control Flow** - If/Else, Match, While/For Loops, Try/Except, Assertions
5. **Functions** - Function basics, Args/Kwargs, Lambda, Scope, Decorators, Context Managers
6. **Collections** - Lists, Tuples, Sets, Dictionaries, Arrays, Comprehensions, Iterators, Generators, itertools, heapq, bisect
7. **Object-Oriented Programming** - Classes, Objects, Inheritance, Polymorphism, Dunder Methods, Dataclasses
8. **Files & Data** - File I/O, Paths (pathlib), JSON, Dates & Times
9. **Quality** - Debugging (pdb), Logging, Testing (unittest/pytest), Type Hints, PEP 8, Property-based Testing
10. **Advanced Topics** - Concurrency, functools, more collections
11. **Typing & Static Analysis** - Type Hints, Generics, Protocols, TypedDict, Type Narrowing, Mypy/Pyright
12. **Error Handling & Robustness** - Exception handling, error recovery patterns
13. **Logging & Observability** - Structured logging, monitoring patterns
14. **Concurrency** - Threading, Multiprocessing, Asyncio
15. **Performance** - Profiling, optimization techniques
16. **Python Internals** - Object model, Descriptors, MRO, Reference Counting, Bytecode
17. **Security** - Input validation, Safe serialization, Secrets management, Hashing
18. **CLI & Automation** - argparse, click/typer, Command structure, Rich/Progress bars
19. **Architecture** - Modularization, Dependency Injection, Hexagonal Architecture, Layered Architecture, Plugin Systems, Design Patterns, Pipelines, DDD
20. **Refactoring** - Code smells, Extract patterns, Composition vs Inheritance, Tooling

### B_DSA

A comprehensive data structures and algorithms curriculum:

1. **Foundations** - Complexity Analysis (Big-O), Recursion, Bit Manipulation
2. **Core Techniques & Paradigms** - Two-Pointer, Sliding Window, Divide-and-Conquer, Meet-in-the-middle
3. **Linear Data Structures** - Arrays, Strings, Linked Lists, Stacks, Queues, Deques
4. **Trees & Hierarchical Structures** - Binary Trees, BST, Balanced Trees (AVL, Red-Black), Heaps, B-Trees, Tries, Segment Trees, Fenwick Trees, Advanced Range Query Structures
5. **String Indexes & Automata** - Suffix Arrays, Suffix Trees, Suffix Automaton, Palindromic Tree, Burrows-Wheeler Transform
6. **Graph & Connectivity** - Graph Representations, Union-Find, BFS/DFS variants, Dynamic Connectivity
7. **Specialized & Probabilistic Structures** - Hash Tables, Skip Lists, Bloom Filters, Count Sketch, Cuckoo Filters
8. **Searching Algorithms** - Linear Search, Binary Search
9. **Sorting Algorithms** - Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix, Bucket, Shell, Timsort
10. **Graph Algorithms** - DFS/BFS Traversals, Shortest Paths (Dijkstra, Bellman-Ford, A*, Floyd-Warshall), MST, Topological Sort, Strongly Connected Components, Matching, Network Flow, Cuts, Eulerian/Hamiltonian Paths
11. **Tree Algorithms & Techniques** - LCA, Heavy-Light Decomposition, Centroid Decomposition, Euler Tour, Rerooting DP
12. **Dynamic Programming** - 1-D/2-D DP, String DP, Tree DP, Bitmask DP, DAG DP, Combinatorial DP, DP Optimizations, Digit DP, Profile DP
13. **Greedy Algorithms** - Activity Scheduling, Huffman Coding, Coin Change
14. **String Algorithms & Pattern Matching** - Naïve Matching, KMP, Z-Algorithm, Rabin-Karp, Aho-Corasick, Manacher's, String Hashing
15. **Backtracking & Search** - Backtracking, Branch-and-Bound, N-Queens, Sudoku Solver, Subset Sum
16. **Selection, Streaming & Sketching** - Quickselect, Median-of-Medians, Count-Min Sketch, HyperLogLog, Misra-Gries, Cuckoo/Consistent Hashing
17. **Offline & Decomposition Techniques** - Mo's Algorithm, Sqrt-decomposition, Coordinate Compression, DSU on Tree
18. **Game Theory** - Basics, Minimax, Alpha-Beta Pruning
19. **Computational Geometry** - Basics, Convex Hull, Line Sweep, Rotating Calipers, Closest Pair, Point-in-Polygon, KD-Trees, Delaunay Triangulation
20. **Number Theory & Combinatorics** - Sieve, Modular Arithmetic, GCD, Modular Inverse, Fast Power, CRT, Matrix Exponentiation, Primality Testing, FFT/NTT
21. **Probabilistic & Randomized** - Reservoir Sampling, Monte Carlo, Las Vegas Algorithms
22. **Parallel & Big Data** - Parallel Algorithms, External-Memory Algorithms, MapReduce

### C_Real_World_Applications

This track contains **end-to-end, real-world style projects** that deliberately sit on top of the Python and DSA paths instead of being mixed into them. Each subfolder is a self-contained mini-application with:

- A focused domain (e.g., automation, data pipeline, API client, small web service).
- A clear `README.md` describing requirements and architecture.
- Minimal but realistic project structure (`src/`, tests, `pyproject.toml` or `requirements.txt`).

Examples of categories you may find here:

- **Automation & DevOps** – backup scripts, log processors, config generators.
- **Data Workflows** – ETL-style mini pipelines using `datasets/`.
- **APIs & Networking** – HTTP clients, small REST-ish backends.
- **CLI Tools** – production-flavored command line apps.

Nothing in `C_Real_World_Applications/` is required to "know Python"; it is where you practice applying the concepts from `A_Python_Core/` and `B_DSA/` in realistic scenarios.

## Features
- **Comprehensive Curriculum**: 42+ major topic categories covering Python and DSA
- **Structured Learning Path**: Organized progression from fundamentals to advanced concepts
- **Practical Examples**: Real code examples demonstrating each concept
- **Exercise Templates**: Starter files for hands-on practice
- **Clear Documentation**: Well-commented code following PEP 8 standards
- **Multiple Difficulty Levels**: Content suitable for beginners through advanced learners
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Modular Design**: Each topic is self-contained for easy navigation

## Getting Started

### Prerequisites
- Follow `A_Python_Core/A.0_Getting_Started/README.md` to install Python, VS Code, and configure PowerShell.
- Git
- Optionally: PowerShell 7+ on Windows for helper scripts

### Installation
```bash
# Clone the repository
git clone https://github.com/yasir-arafat123/Python_Programming.git
cd Python_Programming

# (Optional) Create and activate a virtual environment (see 0_Getting_Started for details)
python -m venv .venv
# Windows
. .venv/Scripts/Activate
# macOS/Linux
source .venv/bin/activate

# (Optional) Install dependencies if a requirements.txt is present
pip install -r requirements.txt
```

## Usage

Each topic folder contains Python scripts with examples and exercises. To explore a topic:

```bash
# Navigate to a specific topic
cd A_Python_Core/A.2_Core/1_Syntax

# Run the main.py file
python main.py
```

For topics with examples and exercises:
```bash
# Run examples
python examples.py

# Run exercises
python exercises.py
```

Many scripts support command-line arguments:
```bash
python path/to/script.py --help
```

> **Tip**: The repository is organized hierarchically. Start with `A_Python_Core` for Python fundamentals, then explore `B_DSA` for algorithms and data structures. See [FOLDER_OVERVIEW.md](FOLDER_OVERVIEW.md) for a complete directory tree.

## PowerShell Helpers
If you are on Windows, you may find PowerShell scripts (e.g., setup, formatting, or quick‑run helpers). To run a script:
```powershell
# Example
./scripts/setup.ps1
```
If you encounter execution policy restrictions, run PowerShell as Administrator:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Tips & Conventions
- Follow PEP 8 for Python style.
- Prefer type hints and docstrings for clarity.
- Use `if __name__ == "__main__":` for script entry points.
- Keep functions small and testable; avoid side effects.
- Add a short README.md in subfolders to explain contents when helpful.

## Contributing
Contributions, suggestions, and improvements are welcome!
1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Commit changes: `git commit -m "feat: add ..."`
4. Push to your fork and open a Pull Request

> For larger changes, consider opening an issue first to discuss the proposal.

## Roadmap

### Current Status
- ✅ Comprehensive Python Core Topics curriculum (20+ categories)
- ✅ Extensive DSA Topics coverage (22+ categories)
- ✅ Project structure with organized folders and templates
- ✅ PowerShell helpers for Windows workflow

### Future Plans
- Add detailed README.md files in each subtopic folder
- Expand examples and exercises in each module
- Include unit tests and CI/CD for code validation
- Add Jupyter notebooks for interactive learning
- Create video tutorials and walkthroughs
- Build a searchable documentation site
- Add more real-world project examples

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Python documentation: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Awesome Python: https://github.com/vinta/awesome-python
