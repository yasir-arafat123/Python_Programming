# Fast & Slow Pointers (Tortoise and Hare)
## Core Pattern
Two pointers moving at different speeds through a sequence.
**Slow**: Moves 1 step per iteration  
**Fast**: Moves 2 steps per iteration
## Key Insight
If there's a cycle, fast eventually catches slow inside the cycle.
## Cycle Detection Algorithm
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
        if slow == fast:
            return True  # Cycle found
    return False  # No cycle
```
## Finding Cycle Start
```python
def detect_cycle(head):
    # Phase 1: Detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # Cycle start node
```
### Why it works?
If cycle length is C and distance to cycle is D:
- They meet at distance D + kC from start
- Reset slow to head, both move 1 step ??? meet at cycle start
## Applications
### 1. Linked List Cycle (LC 141, 142)
Standard cycle detection
### 2. Find Middle of Linked List (LC 876)
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # When fast reaches end, slow at middle
```
### 3. Palindrome Linked List (LC 234)
Find middle ??? reverse second half ??? compare
### 4. Happy Number (LC 202)
Detect cycle in digit sum sequence
### 5. Duplicate Number (LC 287)
Treat array as implicit linked list
## Time/Space Complexity
- **Time**: O(n) for cycle detection
- **Space**: O(1) - constant extra space
## Practice Problems
- LC 141: Linked List Cycle
- LC 142: Linked List Cycle II
- LC 202: Happy Number
- LC 287: Find Duplicate Number
- LC 876: Middle of Linked List
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Application): 3-4 hours
