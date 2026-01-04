"""
Valid Parentheses
Determine if the input string has valid parentheses.
"""

def is_valid_parentheses(s):
    """
    Use stack to check if parentheses are balanced.
    Time: O(n), Space: O(n)
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


# Example usage
if __name__ == "__main__":
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
    ]
    
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"Input: {test:10} -> Valid: {result}")
