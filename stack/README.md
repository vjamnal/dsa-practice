# Stack

Stack-based problems using LIFO (Last In First Out) principle.

## Problems

1. **Valid Parentheses** - Check if brackets are balanced
2. **Min Stack** - Stack with O(1) min operation
3. **Evaluate Reverse Polish Notation** - Evaluate postfix expression
4. **Daily Temperatures** - Find next warmer temperature
5. **Largest Rectangle in Histogram** - Find max rectangle area

## Stack Implementation

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

## Time Complexity

- Push: O(1)
- Pop: O(1)
- Peek: O(1)
