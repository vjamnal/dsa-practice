# problem: Fibonacci Sequence
# approach: Recursion with Memoization
# time: O(n) with memoization, O(2^n) without
# space: O(n)

"""
Fibonacci Sequence
Calculate the nth Fibonacci number using recursion.
"""

def fibonacci_recursive(n):
    """
    Simple recursive solution - O(2^n) time, O(n) space
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    Memoized recursive solution - O(n) time, O(n) space
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """
    Iterative solution - O(n) time, O(1) space
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


if __name__ == "__main__":
    print("Fibonacci Tests:")
    print(f"fib(10) recursive: {fibonacci_recursive(10)}")  # 55
    print(f"fib(10) memoized: {fibonacci_memoization(10)}")  # 55
    print(f"fib(10) iterative: {fibonacci_iterative(10)}")  # 55
