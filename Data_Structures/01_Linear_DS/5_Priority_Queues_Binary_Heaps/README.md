# Priority Queues & Binary Heaps
## Abstract Data Type: Priority Queue
Operations:
- **insert(x)**: Add element with priority
- **extract_min/max()**: Remove & return highest priority
- **peek()**: View highest priority without removing
- **decrease_key(x)**: Update element priority
## Implementation: Binary Heap
### Properties
1. **Complete binary tree** - all levels filled except possibly last
2. **Heap property**:
   - Min-heap: parent ??? children
   - Max-heap: parent ??? children
### Array Representation
For node at index i:
- Parent: (i - 1) // 2
- Left child: 2*i + 1
- Right child: 2*i + 2
### Python heapq Module
```python
import heapq
# Min-heap (default)
heap = []
heapq.heappush(heap, 5)       # O(log n)
heapq.heappush(heap, 3)
min_val = heapq.heappop(heap) # O(log n) ??? 3
# Max-heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
max_val = -heapq.heappop(max_heap)  # 5
# Heapify existing list: O(n)
arr = [5, 3, 7, 1]
heapq.heapify(arr)  # Converts to heap in-place
# K largest/smallest
k_largest = heapq.nlargest(3, arr)   # O(n log k)
k_smallest = heapq.nsmallest(3, arr)
```
### Manual Implementation
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
    def pop(self):
        if not self.heap:
            return None
        # Swap root with last, remove last, bubble down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()
        self._bubble_down(0)
        return min_val
    def _bubble_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._bubble_up(parent)
    def _bubble_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._bubble_down(smallest)
```
## Time Complexity
- Insert: O(log n)
- Extract min/max: O(log n)
- Peek: O(1)
- Heapify: O(n) - builds heap from scratch
- Space: O(n)
## Common Applications
1. **Dijkstra's shortest path** - extract min distance
2. **Heap sort** - O(n log n) sorting
3. **K-th largest element** - maintain min-heap of size k
4. **Merge k sorted lists** - min-heap of list heads
5. **Median maintenance** - two heaps (max + min)
6. **Task scheduling** - priority-based execution
## LeetCode Practice
- LC 215: Kth Largest Element
- LC 23: Merge k Sorted Lists
- LC 295: Find Median from Data Stream
- LC 347: Top K Frequent Elements
- LC 1046: Last Stone Weight
## Time Estimates
- Level 1 (Understanding): 3-4 hours
- Level 2 (Implementation): 4-5 hours
- Level 3 (Applications): 5-6 hours
