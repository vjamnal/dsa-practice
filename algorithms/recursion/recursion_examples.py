"""
Recursion Examples
Classic recursive algorithm implementations.
"""

def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def power(base, exponent):
    """Calculate base raised to exponent."""
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    half = power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    else:
        return base * half * half


def sum_of_digits(n):
    """Calculate sum of digits of a number."""
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def reverse_string(s):
    """Reverse a string using recursion."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


def is_palindrome(s):
    """Check if string is palindrome using recursion."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Tower of Hanoi problem.
    Move n disks from source to destination using auxiliary.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)
