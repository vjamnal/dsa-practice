# Queue

Queue-based problems using FIFO (First In First Out) principle.

## Problems

1. **Implement Queue using Stacks** - Build queue with two stacks
2. **Moving Average from Data Stream** - Calculate moving average
3. **Number of Recent Calls** - Count recent requests
4. **Design Circular Queue** - Circular queue implementation

## Queue Implementation

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def front(self):
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
```

## Time Complexity

- Enqueue: O(1)
- Dequeue: O(n) for list, O(1) for deque
- Front: O(1)
