# Job Sequencing with Deadlines
## Problem
Given n jobs:
- Each job has a **deadline** and **profit**
- Each job takes 1 unit of time
- Maximize profit by scheduling jobs before deadlines
## Greedy Strategy
1. Sort jobs by profit (descending)
2. For each job, schedule in latest available slot before deadline
## Algorithm
```python
def job_sequencing(jobs, max_deadline):
    '''
    jobs: list of (job_id, deadline, profit)
    max_deadline: maximum deadline value
    Returns: (total_profit, scheduled_jobs)
    '''
    # Sort by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)
    # Track occupied time slots
    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    scheduled = []
    for job_id, deadline, profit in jobs:
        # Find latest available slot before deadline
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] == -1:  # Slot available
                slots[slot] = job_id
                total_profit += profit
                scheduled.append(job_id)
                break
    return total_profit, scheduled
# Example
jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]
profit, schedule = job_sequencing(jobs, 3)
print(f"Max profit: {profit}")  # 142
print(f"Schedule: {schedule}")  # ['A', 'C', 'E']
```
## Optimized with Disjoint Set (Union-Find)
```python
def find_latest_slot(parent, slot):
    '''Find latest available slot using path compression'''
    if parent[slot] == slot:
        return slot
    parent[slot] = find_latest_slot(parent, parent[slot])
    return parent[slot]
def job_sequencing_optimized(jobs, max_deadline):
    jobs.sort(key=lambda x: x[2], reverse=True)
    # Union-Find: parent[i] = latest available slot <= i
    parent = list(range(max_deadline + 1))
    total_profit = 0
    scheduled = []
    for job_id, deadline, profit in jobs:
        # Find latest available slot
        available_slot = find_latest_slot(parent, min(deadline, max_deadline))
        if available_slot > 0:  # Slot found
            scheduled.append(job_id)
            total_profit += profit
            # Mark slot as occupied, point to next available
            parent[available_slot] = find_latest_slot(parent, available_slot - 1)
    return total_profit, scheduled
```
## Complexity
- **Naive**: O(n?? ) - for each job, scan slots
- **Optimized (Union-Find)**: O(n log n) - sorting + ??(n) per job
## Why Greedy Works
**Exchange argument:**
- If optimal swaps high-profit job for low-profit ??? less profit
- Taking highest profit first is always safe
## Practice Problems
- Job sequencing with deadlines
- Maximum profit job scheduling (LC 1235) - DP variant
- Task scheduler (LC 621)
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Implementation): 3-4 hours
