# Linked List

Linked list problems and implementations.

## Problems

1. **Reverse Linked List** - Reverse a singly linked list
2. **Merge Two Sorted Lists** - Merge two sorted linked lists
3. **Linked List Cycle** - Detect cycle in linked list
4. **Remove Nth Node From End** - Remove node from end
5. **Intersection of Two Linked Lists** - Find intersection point

## Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Common Techniques

- Two pointers (fast and slow)
- Dummy node
- Recursion
- Reversing links

## Time Complexity

- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) elsewhere
- Deletion: O(1) with pointer, O(n) to find
