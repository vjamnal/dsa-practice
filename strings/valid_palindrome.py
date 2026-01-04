# problem: Valid Palindrome
# approach: Two Pointers
# time: O(n)
# space: O(1)

"""
Valid Palindrome
Check if a string is a palindrome, considering only alphanumeric characters.

LeetCode #125
"""

def is_palindrome(s):
    """
    Two pointer approach - O(n) time, O(1) space
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    print("Valid Palindrome Tests:")
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome(" "))  # True
