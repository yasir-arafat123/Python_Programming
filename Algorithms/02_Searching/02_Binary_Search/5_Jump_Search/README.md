# Jump Search
## When to Use
- **Sorted arrays** where binary search overhead is high
- **Linear memory access** is cheaper than random access (cache-friendly)
- Between linear and binary search in performance
## How It Works
1. Jump ahead by fixed steps (???n optimal)
2. Linear search backwards in block when overshot
## Algorithm
```python
import math
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0
    # Jump until we overshoot
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Not found
    # Linear search in block [prev, min(step, n))
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1  # Not found
    # Check if we found it
    if arr[prev] == target:
        return prev
    return -1
```
## Time Complexity
- **Time**: O(???n)
  - Jump phase: O(???n)
  - Linear search: O(???n)
- **Space**: O(1)
- **Comparisons**: ~???n (better than linear's n, worse than binary's log n)
## Why Use Jump Search?
1. **Cache-friendly**: Linear memory access in blocks
2. **Better than linear**: O(???n) vs O(n)
3. **Simpler than binary**: No recursion/complex indexing
4. **Backward jumps**: Easier to implement than interpolation search
## Optimal Jump Size
Why ???n?
- Too small ??? more jumps (like linear)
- Too large ??? more backward steps
- ???n balances both phases
## Example: Find First Occurrence
```python
def jump_search_first(arr, target):
    '''Find first occurrence using jump search'''
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    # Jump until overshoot
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
    # Linear search for first occurrence
    result = -1
    while prev < min(step, n):
        if arr[prev] == target:
            return prev  # First occurrence
        elif arr[prev] > target:
            break
        prev += 1
    return -1
```
## Comparison with Other Searches
| Algorithm | Time | Space | Best For |
|-----------|------|-------|----------|
| Linear | O(n) | O(1) | Unsorted, small arrays |
| Jump | O(???n) | O(1) | Cache-friendly sorted |
| Binary | O(log n) | O(1) | General sorted arrays |
| Interpolation | O(log log n) avg | O(1) | Uniformly distributed |
## Practice
1. Implement jump search
2. Compare with binary search on large arrays
3. Measure cache misses (binary vs jump)
## Time Estimates
- Level 1 (Understanding): 1-2 hours
- Level 2 (Implementation): 1-2 hours
