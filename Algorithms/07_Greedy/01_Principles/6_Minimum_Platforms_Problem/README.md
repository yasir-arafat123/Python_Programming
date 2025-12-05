# Minimum Platforms Problem
## Problem
Given arrival and departure times of trains:
- Find minimum platforms needed so no train waits
Equivalent: **Minimum meeting rooms** (LC 253)
## Greedy Strategy
Sort all events (arrivals & departures), track concurrent trains.
## Algorithm
```python
def min_platforms(arrivals, departures):
    '''
    arrivals: list of arrival times
    departures: list of departure times
    Returns: minimum platforms needed
    '''
    arrivals.sort()
    departures.sort()
    platforms_needed = 0
    max_platforms = 0
    i = j = 0
    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            # Train arrives before one departs
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            # Train departs, free a platform
            platforms_needed -= 1
            j += 1
    return max_platforms
# Example
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arrivals, departures))  # 3
# At 1100: trains at 940, 950, 1100 all present ??? 3 platforms
```
## Alternative: Sweep Line Algorithm
```python
def min_platforms_sweep(arrivals, departures):
    '''Using event sorting'''
    events = []
    for time in arrivals:
        events.append((time, 1))  # +1 for arrival
    for time in departures:
        events.append((time, -1))  # -1 for departure
    events.sort(key=lambda x: (x[0], x[1]))  # Sort by time, then type
    # (arrival before departure if same time)
    platforms = 0
    max_platforms = 0
    for time, event_type in events:
        platforms += event_type
        max_platforms = max(max_platforms, platforms)
    return max_platforms
```
## LeetCode 253: Meeting Rooms II
```python
def min_meeting_rooms(intervals):
    '''
    intervals: list of [start, end] intervals
    Returns: minimum meeting rooms needed
    '''
    if not intervals:
        return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    rooms = 0
    max_rooms = 0
    s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    return max_rooms
```
## Complexity
- **Time**: O(n log n) - sorting dominates
- **Space**: O(1) if sorting in-place, else O(n)
## Why Greedy Works
At any time, platforms needed = concurrent trains = overlapping intervals.
## Practice Problems
- LC 253: Meeting Rooms II
- LC 252: Meeting Rooms (can attend all?)
- Minimum platforms (GFG)
- Car pooling (LC 1094)
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Implementation): 2-3 hours
