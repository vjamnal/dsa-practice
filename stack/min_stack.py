# problem: Min Stack
# approach: Two Stacks (main + min tracker)
# time: O(1) for all operations
# space: O(n)

"""
Min Stack
Stack that supports push, pop, top, and retrieving minimum element in O(1).

LeetCode #155
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    print("Min Stack Tests:")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"Min: {min_stack.get_min()}")  # -3
    min_stack.pop()
    print(f"Top: {min_stack.top()}")  # 0
    print(f"Min: {min_stack.get_min()}")  # -2
