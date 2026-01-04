# problem: Valid Parentheses
# approach: Stack
# time: O(n)
# space: O(n)

"""
Valid Parentheses
Determine if the input string has valid parentheses.

LeetCode #20
"""

def is_valid(s):
    """
    Stack-based approach - O(n) time, O(n) space
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


if __name__ == "__main__":
    print("Valid Parentheses Tests:")
    print(is_valid("()"))  # True
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))  # False
    print(is_valid("([)]"))  # False
    print(is_valid("{[]}"))  # True
