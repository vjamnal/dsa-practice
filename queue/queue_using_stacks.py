# problem: Implement Queue using Stacks
# approach: Two Stacks (in and out)
# time: O(1) amortized for all operations
# space: O(n)

"""
Implement Queue using Stacks
Implement a queue using two stacks.

LeetCode #232
"""

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x):
        """Push element to the back of queue - O(1)"""
        self.stack_in.append(x)
    
    def pop(self):
        """Remove element from front of queue - O(1) amortized"""
        self._move()
        return self.stack_out.pop()
    
    def peek(self):
        """Get the front element - O(1) amortized"""
        self._move()
        return self.stack_out[-1]
    
    def empty(self):
        """Return whether queue is empty - O(1)"""
        return not self.stack_in and not self.stack_out
    
    def _move(self):
        """Move elements from stack_in to stack_out if needed"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


if __name__ == "__main__":
    print("Queue using Stacks Tests:")
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(f"Peek: {queue.peek()}")  # 1
    print(f"Pop: {queue.pop()}")  # 1
    print(f"Empty: {queue.empty()}")  # False
