# problem: Palindrome Number
# approach: Math - Reverse half of number
# time: O(log n) - number of digits
# space: O(1)

"""
Palindrome Number
Determine if an integer is a palindrome without converting to string.

LeetCode #9
"""

def is_palindrome(x):
    """
    Reverse half of the number and compare
    """
    # Negative numbers and numbers ending in 0 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # For even length: x == reversed_half
    # For odd length: x == reversed_half // 10
    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    print("Palindrome Number Tests:")
    print(is_palindrome(121))  # True
    print(is_palindrome(-121))  # False
    print(is_palindrome(10))  # False
