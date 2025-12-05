# Development Skills & Quality Engineering

Core: Testing, linting, formatting, type checking, CI, documentation, refactoring, security scanning, and release workflow.

## Subtopics
1. 01_Linting_ruff_flake8
2. 02_Formatting_black_isort
3. 03_Type_Checking_mypy_pyright
4. 04_Testing_pytest_unittest
5. 05_Test_Doubles_mocks_fixtures
6. 06_Coverage_metrics
7. 07_CI_Basics_GitHub_Actions
8. 08_PreCommit_Hooks
9. 09_Refactoring_Strategies
10. 10_Code_Smells_AntiPatterns
11. 11_Documentation_Docstrings_Styles
12. 12_Doc_Build_Sphinx_MkDocs
13. 13_Changelogs_SemVer_Release_Process
14. 14_Security_Static_Scanning_bandit

## Learning Outcomes
- Establish a reproducible quality toolchain.
- Differentiate lint vs format vs type check.
- Create maintainable test suites with fixtures and mocks.
- Automate quality gates in CI with pre-commit hooks.
- Manage semantic versioning and release notes.
- Integrate static security analysis early.

## Suggested Folder Pattern
Each subfolder contains: `overview.md`, `examples/`, `exercises.md`, and optional `tooling/` config samples.

## Exercises
1. Configure ruff + black + mypy in a sample project.
2. Add pytest fixture that writes to `tmp_path` and assert output.
3. Add pre-commit config and simulate a failing hook.
4. Create a GitHub Actions workflow running lint, tests, type check, coverage.
5. Write docstring in Google and NumPy style; generate Sphinx docs.

## References
- Ruff: https://github.com/astral-sh/ruff
- Pytest docs: https://docs.pytest.org/
- Mypy: https://mypy.readthedocs.io/
- Pre-commit: https://pre-commit.com/
- Bandit: https://bandit.readthedocs.io/

