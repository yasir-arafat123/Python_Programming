# Circular Buffers (Ring Buffers)
## Concept
Fixed-size buffer that wraps around when reaching the end. Old data is overwritten when buffer is full.
## Use Cases
- **Streaming data** - audio, video, logs
- **Producer-consumer** - bounded queue
- **LRU cache** - circular eviction
- **Windowing** - sliding window averages
## Implementation
```python
class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0  # Write position
        self.tail = 0  # Read position
        self.size = 0
    def enqueue(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        if self.size == self.capacity:
            # Overwrite: advance tail
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Buffer empty")
        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item
    def is_full(self):
        return self.size == self.capacity
    def is_empty(self):
        return self.size == 0
```
## Python collections.deque
```python
from collections import deque
# Fixed-size circular buffer
buffer = deque(maxlen=5)
buffer.append(1)  # [1]
buffer.append(2)  # [1, 2]
buffer.extend([3, 4, 5])  # [1, 2, 3, 4, 5]
buffer.append(6)  # [2, 3, 4, 5, 6] - overwrites 1
# Efficient O(1) operations
buffer.appendleft(0)  # [0, 2, 3, 4, 5]
buffer.pop()          # 5
buffer.popleft()      # 0
```
## Design Circular Queue (LC 622)
```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.head + self.size) % self.capacity
        self.queue[idx] = value
        self.size += 1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.head + self.size - 1) % self.capacity
        return self.queue[idx]
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.capacity
```
## Time Complexity
- Enqueue: O(1)
- Dequeue: O(1)
- Peek front/rear: O(1)
- Space: O(k) for capacity k
## Practice Problems
- LC 622: Design Circular Queue
- LC 641: Design Circular Deque
- LC 933: Number of Recent Calls (sliding window)
## Time Estimates
- Level 1 (Understanding): 2-3 hours
- Level 2 (Implementation): 2-3 hours
