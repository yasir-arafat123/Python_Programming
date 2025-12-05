# Prefix Sums & Difference Arrays
## Prefix Sums (Cumulative Sums)
**Purpose**: Answer range sum queries in O(1) after O(n) preprocessing
### Algorithm
```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix
def range_sum(prefix, left, right):  # O(1)
    return prefix[right + 1] - prefix[left]
```
### 2D Prefix Sums
```python
# prefix[i][j] = sum of rectangle (0,0) to (i-1,j-1)
def build_2d_prefix(matrix):
    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (matrix[i-1][j-1] +
                           prefix[i-1][j] +
                           prefix[i][j-1] -
                           prefix[i-1][j-1])
    return prefix
```
## Difference Arrays
**Purpose**: Apply range updates in O(1), then reconstruct in O(n)
### Algorithm
```python
def range_update(arr, queries):
    n = len(arr)
    diff = [0] * (n + 1)
    # Apply all range updates: O(q)
    for left, right, val in queries:
        diff[left] += val
        diff[right + 1] -= val
    # Reconstruct final array: O(n)
    result = [0] * n
    result[0] = arr[0] + diff[0]
    for i in range(1, n):
        diff[i] += diff[i-1]
        result[i] = arr[i] + diff[i]
    return result
```
## Common Use Cases
1. **Subarray sum queries** - Prefix sums
2. **Range increment/decrement** - Difference arrays
3. **Count frequency in ranges** - 2D prefix sums
4. **Maximum subarray sum** - Kadane's with prefix
5. **Equilibrium index** - Prefix from both ends
## LeetCode Practice
- LC 303: Range Sum Query - Immutable
- LC 304: Range Sum Query 2D - Immutable
- LC 560: Subarray Sum Equals K
- LC 1094: Car Pooling (difference array)
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Practice): 4-5 hours
