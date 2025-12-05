# Exponential Search (Galloping Search)
## When to Use
- **Unbounded/infinite arrays** where size is unknown
- **Target near beginning** - faster than binary search
- Useful when binary search range is costly to determine
## How It Works
1. Find range where element exists (exponentially increasing jumps)
2. Perform binary search in that range
## Algorithm
```python
def exponential_search(arr, target):
    n = len(arr)
    # Special case: first element
    if arr[0] == target:
        return 0
    # Find range: [i/2, min(i, n-1)]
    i = 1
    while i < n and arr[i] <= target:
        i *= 2  # Exponential growth
    # Binary search in [i//2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
## Time Complexity
- **Best case**: O(1) - element at first position
- **Average case**: O(log i) where i is target position
  - Range finding: O(log i)
  - Binary search: O(log i)
  - Total: O(log i)
- **Worst case**: O(log n)
- **Space**: O(1)
## Why Better Than Binary Search?
When target is near beginning:
- Binary search: Always O(log n)
- Exponential: O(log i) where i << n
## Example: Search in Infinite Array
```python
class ArrayReader:
    def get(self, index):
        # Returns element at index or sys.maxsize if out of bounds
        pass
def search_infinite(reader, target):
    '''LC 702: Search in a Sorted Array of Unknown Size'''
    # Find upper bound
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right *= 2  # Exponential jump
    # Binary search in [left, right]
    while left <= right:
        mid = (left + right) // 2
        val = reader.get(mid)
        if val == target:
            return mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
## Applications
1. **Unbounded binary search** - unknown array size
2. **Galloping in merge** - merge sorted lists efficiently
3. **Skip lists** - probabilistic data structures
4. **Database indexing** - when records near start
## Practice Problems
- LC 702: Search in Sorted Array of Unknown Size
- Find position in infinite sorted array
## Time Estimates
- Level 1 (Understanding): 1-2 hours
- Level 2 (Implementation): 1-2 hours
