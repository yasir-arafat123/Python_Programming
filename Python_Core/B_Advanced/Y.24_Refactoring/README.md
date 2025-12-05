# Refactoring & Maintainability

Aim: Systematically improve code without changing behavior; recognize and eliminate smells.

## Subtopics
1. 01_Identify_Code_Smells
2. 02_Extract_Function_Object
3. 03_Composition_vs_Inheritance
4. 04_Simplifying_Conditionals
5. 05_State_Elimination_with_Data
6. 06_Test_Supported_Refactors
7. 07_Tooling_for_Refactoring (rope, IDE, codemods)
8. 08_Metrics_Cyclomatic_Coupling (lightweight)

## Learning Outcomes
- Detect common Python smell patterns (long function, shotgun surgery, feature envy).
- Apply surgical refactors with safety via tests.
- Replace conditionals with polymorphism or lookup tables.
- Use tools to automate repetitive refactors.

## Exercises
- Refactor a 150-line function into cohesive units.
- Replace nested if ladder with strategy map.
- Introduce dataclass to remove parallel lists smell.
