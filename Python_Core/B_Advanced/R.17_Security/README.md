# Security & Reliability

Focus: Writing safer Python code; avoiding common pitfalls in secrets handling, serialization, sandboxing, and dependency risk.

## Subtopics (Initial + New Adds)
1. 01_Input_Validation
2. 02_Avoiding_eval_exec
3. 03_Safe_Serialization_pickle_dangers
4. 04_Secrets_Management_environment
5. 05_Hashing_HMAC_compare_digest
6. 06_Dependency_Scanning_pip_audit_safety
7. 07_Least_Privilege_File_Perms
8. 08_Temporary_Files_Secure_Usage
9. 09_Configuration_Secrets_vs_Config
10. 10_Sandboxing_Limits (conceptual)

## Learning Outcomes
- Distinguish configuration vs secret vs code.
- Use secure hashing & timing-safe comparisons.
- Identify insecure patterns (pickle untrusted, eval, broad except).
- Employ tools: `pip-audit`, `safety`, `bandit`.

## Exercises
- Replace insecure `eval` usage with safe parser.
- Demonstrate pickle RCE payload and mitigation.
- Build a secrets loader (env + .env + fallback) with validation.
