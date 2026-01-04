# problem: Best Time to Buy and Sell Stock II
# approach: Greedy (Add all positive differences)
# time: O(n)
# space: O(1)

"""
Best Time to Buy and Sell Stock II
Find maximum profit with multiple transactions.

LeetCode #122
"""

def max_profit(prices):
    """
    Greedy approach - O(n) time, O(1) space
    Add profit whenever price increases
    """
    if not prices:
        return 0
    
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    
    return profit


if __name__ == "__main__":
    print("Best Time to Buy and Sell Stock II Tests:")
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 7
    print(max_profit([1, 2, 3, 4, 5]))  # 4
    print(max_profit([7, 6, 4, 3, 1]))  # 0
