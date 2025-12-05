# Ternary Search
## When to Use
- **Unimodal functions**: Single peak (maximum) or valley (minimum)
- Finding optimal value in convex/concave functions
- Alternative to golden section search
## How It Works
Divide search space into THREE parts (vs binary's two).
Eliminates 1/3 of space per iteration.
## Algorithm
```python
def ternary_search_max(f, left, right, epsilon=1e-9):
    '''Find maximum of unimodal function f in [left, right]'''
    while right - left > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if f(mid1) < f(mid2):
            left = mid1  # Maximum in [mid1, right]
        else:
            right = mid2  # Maximum in [left, mid2]
    return (left + right) / 2
# For finding minimum, flip condition:
# if f(mid1) > f(mid2): left = mid1
```
## Discrete Ternary Search
```python
def ternary_search_discrete(arr):
    '''Find peak element in mountain array'''
    left, right = 0, len(arr) - 1
    while left < right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        else:
            right = mid2 - 1
    return left  # Peak index
```
## Complexity
- **Time**: O(log??? n) ??? 1.585 * O(log??? n) - Worse than binary search!
- **Space**: O(1)
- **Comparisons**: 2 per iteration (binary search: 1)
## Why Use Ternary Search?
- Works on unimodal functions (binary search needs monotonic)
- Useful when function evaluation is cheap
- Geometric problems (minimum distance, maximum area)
## Example: Maximum in Bitonic Array
```python
def find_peak(arr):
    '''LC 852: Peak Index in Mountain Array'''
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Ascending, peak on right
        else:
            right = mid  # Descending, peak on left or at mid
    return left
```
## Practice Problems
- LC 852: Peak Index in Mountain Array
- LC 162: Find Peak Element
- Minimize maximum distance to gas station (Codeforces)
## Time Estimates
- Level 1 (Understanding): 1-2 hours
- Level 2 (Application): 2-3 hours
