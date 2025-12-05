# Fractional Knapsack (Greedy Solution)
## Problem
Given items with weights and values, and a knapsack with capacity W:
- Can take **fractions** of items (unlike 0/1 knapsack)
- Maximize total value without exceeding capacity
## Key Insight
**Greedy choice**: Sort by value-to-weight ratio, take highest ratio first.
## Algorithm
```python
def fractional_knapsack(items, capacity):
    '''
    items: list of (value, weight) tuples
    capacity: knapsack capacity
    Returns: maximum total value
    '''
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    remaining_capacity = capacity
    for value, weight in items:
        if remaining_capacity >= weight:
            # Take entire item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break  # Knapsack full
    return total_value
# Example
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
print(fractional_knapsack(items, capacity))  # 240
# Take: 10kg@6/kg + 20kg@5/kg + 20kg@4/kg = 60 + 100 + 80 = 240
```
## Why Greedy Works
**Proof by exchange argument:**
- Suppose optimal solution takes lower ratio before higher
- Swapping them increases total value ??? contradiction
## Complexity
- **Time**: O(n log n) - sorting dominates
- **Space**: O(1) if sorting in-place
## Comparison: 0/1 vs Fractional Knapsack
| Property | 0/1 Knapsack | Fractional Knapsack |
|----------|--------------|---------------------|
| Item splits | ??? No | ??? Yes |
| Greedy works? | ??? No (needs DP) | ??? Yes |
| Complexity | O(nW) DP | O(n log n) sorting |
## Example Problems
### Activity Selection (Related)
```python
def max_activities(start, finish):
    '''Maximum non-overlapping activities - greedy by earliest finish'''
    activities = sorted(zip(finish, start))
    count = 1
    last_finish = activities[0][0]
    for finish_time, start_time in activities[1:]:
        if start_time >= last_finish:
            count += 1
            last_finish = finish_time
    return count
```
## Practice Problems
- Fractional knapsack implementation
- Activity selection (LC 435)
- Meeting rooms (LC 253)
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Implementation): 1-2 hours
