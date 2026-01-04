# problem: Climbing Stairs
# approach: Dynamic Programming (Fibonacci pattern)
# time: O(n)
# space: O(1)

"""
Climbing Stairs
Count the number of ways to climb n stairs (1 or 2 steps at a time).

LeetCode #70
"""

def climb_stairs(n):
    """
    Dynamic programming - O(n) time, O(1) space
    Similar to Fibonacci sequence
    """
    if n <= 2:
        return n
    
    prev, curr = 1, 2
    
    for i in range(3, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def climb_stairs_dp_array(n):
    """
    DP with array - O(n) time, O(n) space
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


if __name__ == "__main__":
    print("Climbing Stairs Tests:")
    print(f"climb_stairs(2): {climb_stairs(2)}")  # 2
    print(f"climb_stairs(3): {climb_stairs(3)}")  # 3
    print(f"climb_stairs(5): {climb_stairs(5)}")  # 8
