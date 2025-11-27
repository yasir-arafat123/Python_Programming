# Folder Overview

A quick, human-friendly snapshot of the `py` workspace. Each top-level topic links to deeper lessons that already contain their own `README.md` and `main.py` templates.

```
py/
├── README.md                ← roadmap + global references
├── FOLDER_OVERVIEW.md       ← this file
├── 01_Python_Core_Topics/
│   ├── 1_Setup_Packaging/
│   │   ├── 1_PIP/
│   │   ├── 2_VirtualEnv/
│   │   ├── 3_Modules_Imports_Packages/
│   │   └── 4_Project_Structure_src_layout_pyproject.toml/
│   ├── 2_Core/
│   │   ├── 1_Syntax/
│   │   ├── 2_Comments/
│   │   ├── …
│   │   └── 10_User_Input_Output/
│   ├── 3_Strings/
│   ├── 4_ControlFlow/
│   ├── 5_Functions/
│   ├── 6_Collections/
│   ├── 7_OOP/
│   ├── 8_Files_Data/
│   ├── 9_Quality/
│   └── 10_Advanced/ … 24_Refactoring/
├── 02_DSA_Topics/
│   ├── 1_Foundations/
│   │   ├── 1_Complexity_Analysis_…/
│   │   ├── 2_Recursion_Mathematical_Induction/
│   │   └── 3_Bit_Manipulation_basics/
│   ├── 2_Core_Techniques_Paradigms/
│   ├── 3_Data_Structures_Linear/
│   ├── …
│   └── 22_Parallel_External-Memory_Big_Data/
└── INDEX/
    └── README.md
```

## Tips for richer visualization

- **VS Code**: use the built-in Explorer outline or install the *TreeView* or *Project Manager* extensions to save filtered views.
- **CLI (PowerShell)**: `Get-ChildItem -Recurse | tree` style tools like `Get-ChildItem -Name -Depth 2` (PowerShell 7+ with `Get-ChildItem -Depth`).
- **Python script**: use the `anytree` or `treelib` packages to generate diagrams, optionally exporting to HTML/SVG for interactive navigation.
- **Markdown diagrams**: convert sections of the tree into Mermaid diagrams for documentation sites.

Update this file whenever the curriculum structure changes so collaborators can see the hierarchy at a glance.
