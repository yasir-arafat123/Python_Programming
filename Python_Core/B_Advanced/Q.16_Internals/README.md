# Python Internals & Data Model

Goal: Understand how Python represents objects, resolves attributes, manages memory, and executes bytecode.

## Subtopics
1. 01_Object_Model_identity_mutability
2. 02_Descriptors_Detail
3. 03_Method_Resolution_Order
4. 04_Name_Mangling_private_convention
5. 05_Slots_Impact
6. 06_String_and_Int_Interning
7. 07_Reference_Counting_GC
8. 08_Bytecode_disassembly
9. 09_Performance_Implications_of_Internals
10. 10_Implementation_Differences

## Learning Outcomes
- Predict attribute lookup order.
- Explain descriptor vs property.
- Discuss refcounting & cyclic GC interplay.
- Read basic dis output to guide optimization.

## Exercises
- Implement a descriptor for type validation.
- Inspect refcounts before/after circular references.
- Compare class with and without __slots__ memory usage.
