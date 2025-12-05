# Master Theorem
## Standard Form
T(n) = aT(n/b) + f(n)
Where:
- a = number of recursive calls
- n/b = problem size reduction
- f(n) = work outside recursion (combine cost)
## Three Cases
### Case 1: f(n) = O(n^(log_b(a) - ??))
Recursion dominates ??? **T(n) = ??(n^log_b(a))**
Example: Binary tree traversal T(n) = 2T(n/2) + O(1) ??? O(n)
### Case 2: f(n) = ??(n^log_b(a))
Equal work ??? **T(n) = ??(n^log_b(a) * log n)**
Example: Merge sort T(n) = 2T(n/2) + O(n) ??? O(n log n)
### Case 3: f(n) = ??(n^(log_b(a) + ??))
Combine dominates ??? **T(n) = ??(f(n))**
Example: T(n) = 2T(n/2) + O(n??) ??? O(n??)
## Common Patterns
- Binary search: T(n) = T(n/2) + O(1) ??? O(log n)
- Merge sort: T(n) = 2T(n/2) + O(n) ??? O(n log n)
- Karatsuba multiply: T(n) = 3T(n/2) + O(n) ??? O(n^1.585)
- Strassen matrix: T(n) = 7T(n/2) + O(n??) ??? O(n^2.807)
## Python Examples
```python
def merge_sort(arr):
    # T(n) = 2T(n/2) + O(n)
    # ??? Case 2: O(n log n)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # T(n/2)
    right = merge_sort(arr[mid:]) # T(n/2)
    return merge(left, right)     # O(n)
```
## Practice
1. Analyze quicksort: T(n) = 2T(n/2) + O(n)
2. Analyze binary tree height: T(n) = 2T(n/2) + O(1)
3. Compare merge vs quick sort recurrences
4. Analyze Strassen's algorithm
## Time Estimates
- Level 1 (Understanding): 3-4 hours
- Level 2 (Application): 4-5 hours
## Resources
- CLRS Chapter 4.5
- [Visualgo Recursion Tree](https://visualgo.net/en/recursion)
