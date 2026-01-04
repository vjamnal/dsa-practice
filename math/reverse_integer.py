# problem: Reverse Integer
# approach: Math - Modulo and division
# time: O(log n) - number of digits
# space: O(1)

"""
Reverse Integer
Reverse the digits of a signed 32-bit integer.

LeetCode #7
"""

def reverse_integer(x):
    """
    Math approach using modulo and division
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = 0
    
    while x:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    result = sign * reversed_num
    
    # Check for 32-bit integer overflow
    if result < -2**31 or result > 2**31 - 1:
        return 0
    
    return result


if __name__ == "__main__":
    print("Reverse Integer Tests:")
    print(reverse_integer(123))  # 321
    print(reverse_integer(-123))  # -321
    print(reverse_integer(120))  # 21
