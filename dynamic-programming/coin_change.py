# problem: Coin Change
# approach: Dynamic Programming (Bottom-up)
# time: O(amount * n) where n is number of coins
# space: O(amount)

"""
Coin Change
Find minimum number of coins needed to make the given amount.

LeetCode #322
"""

def coin_change(coins, amount):
    """
    Dynamic programming - O(amount * n) time, O(amount) space
    where n is number of coin denominations
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print("Coin Change Tests:")
    print(coin_change([1, 2, 5], 11))  # 3 (5 + 5 + 1)
    print(coin_change([2], 3))  # -1 (impossible)
    print(coin_change([1], 0))  # 0
