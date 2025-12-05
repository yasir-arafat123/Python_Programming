# Space Complexity Exercises

## Warm-up Quiz (10 min)
1. Explain the difference between *total* space usage and *auxiliary* space.
2. Why can a divide-and-conquer algorithm such as binary search claim O(log n) space even though it only stores three integers per recursive call?
3. When does Python reuse stack frames or tail-call optimize recursion? (Hint: it does not—describe the implication.)
4. A solution allocates a `dict` with `n` entries where each entry stores a 2-tuple of integers. What is the asymptotic auxiliary space and what constant factors should be mentioned for Python specifically?

## Implementation Drills (30–40 min)
1. **Cyclic rotation in-place**  
   Implement `rotate(nums: list[int], k: int) -> None` that rotates the array to the right by `k` using only O(1) extra space. Avoid allocating helper arrays; rely on reversal cycles.  
   *Verify*: call the function on `[1,2,3,4,5,6,7]` with `k=3` and confirm you get `[5,6,7,1,2,3,4]`.
2. **Constant-space palindrome check**  
   Implement `is_palindrome(head: ListNode) -> bool` for a singly linked list using O(1) extra space. The typical pattern clones or uses a stack—this drill requires: find midpoint, reverse second half in-place, compare, then restore the list.  
   *Learning goals*: practice distinguishing between temporary heap allocations vs pointer rewiring.  
   *Verify*: cover even/odd list lengths and confirm the list structure is restored.
3. **Sliding window sums without arrays**  
   Recreate the `rolling_window_sum` idea from `examples.py`, but expose it as a generator `def sliding_window_values(nums: list[int], k: int) -> Iterator[int]: ...` that yields each sum without storing the entire result.  
   *Verify*: iterate the generator twice (should restart) or document why the generator can only be consumed once.

## Stretch / Variations (20+ min)
1. **DP table compression**  
   Take a classic 0/1 knapsack DP solution that uses an `n x capacity` table. Rewrite it to use a 1D array updated right-to-left so the auxiliary space drops from O(n * capacity) to O(capacity). Provide a short proof sketch that the optimized version returns the same answers.  
   *Verify*: Run both versions on a small instance and diff their outputs.
2. **Recursion depth guard**  
   Given a recursive DFS that risks blowing the call stack on skewed trees, redesign it to be iterative. Track the explicit stack size and compare it with Python's recursion limit (`sys.getrecursionlimit()`). Explain how this affects asymptotic space and practical memory overhead.  
   *Verify*: benchmark both approaches on a line-shaped tree of 10_000 nodes and note which one crashes first.

Estimated total effort: 60–80 minutes including verification and write-up.
