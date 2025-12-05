# Error Handling & Robustness

Focus: Designing resilient Python code via custom exceptions, context managers, retries, warnings, and defensive programming.

## Subtopics
1. 01_Custom_Exception_Hierarchy
2. 02_Contextlib_suppress_exitstack
3. 03_Retry_Patterns_backoff
4. 04_Assertions_vs_Exceptions
5. 05_Warnings_filters
6. 06_Defensive_Programming_Principles

## Learning Outcomes
- Build clear exception hierarchies with meaningful names.
- Leverage context managers for safe resource handling.
- Implement safe retry logic with backoff and cancellation.
- Distinguish assert vs runtime validation.
- Use warnings module responsibly.

## Patterns
- EAFP vs LBYL
- Fail fast vs degrade gracefully
- Guard clauses

## Exercises
- Wrap a file operation with a custom context manager that logs failures.
- Implement an exponential backoff decorator.
- Refactor nested try/except into clearer structure.
