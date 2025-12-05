# Object-Oriented Programming (Expanded)

This module moves from basic class definitions to Python's data model, descriptor protocol, structural subtyping, and composition-oriented design.

## Core Progression
1. Concepts & Motivation
2. Classes & Instances
3. Inheritance vs Composition
4. Polymorphism & Interfaces
5. Dunder / Data Model Methods
6. Descriptors & Properties
7. Abstract Base Classes (abc)
8. Dataclasses, `__slots__`, namedtuple
9. Enums & Flags
10. Protocols (PEP 544) / Structural Subtyping
11. Mixins & Reusable Behaviors
12. Operator Overloading & Rich Comparisons

## Learning Outcomes
- Design clear class hierarchies minimizing depth.
- Implement Pythonic protocols (iterable, context manager, mapping, numeric).
- Use descriptors for validation, caching, delegation.
- Decide between dataclass vs manual `__init__` vs attrs/pydantic.
- Apply structural typing with Protocol to reduce inheritance.

## Design Principles Highlighted
- Composition over inheritance
- LSP (Liskov Substitution) and interface design
- Cohesion & coupling metrics (informally)
- Favor protocols and duck typing when rigid hierarchy hurts flexibility

## Exercises
1. Refactor inheritance-heavy design into composition + Protocol.
2. Implement a descriptor that enforces type + range.
3. Create a dataclass and compare memory with and without `slots=True`.
4. Add rich comparisons to a value object (sorting, hashing considerations).

## Suggested Folder Pattern for New Additions
Add subfolders for: `06_Descriptors_property_static_class/`, `07_Abstract_Base_Classes_abc/`, `08_Dataclasses_Slots_namedtuple/`, `09_Enum_Flag/`, `10_Protocols_Structural_Subtyping/`, `11_Mixins_Composition/`, `12_Operator_Overloading_Rich_Comparison/`.

Each subfolder: `overview.md`, `examples.py`, `exercises.md`.

