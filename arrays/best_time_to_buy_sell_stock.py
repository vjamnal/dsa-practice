# problem: Best Time to Buy and Sell Stock
# approach: One pass tracking minimum price
# time: O(n)
# space: O(1)

"""
Best Time to Buy and Sell Stock
Find the maximum profit from buying and selling a stock once.

LeetCode #121
"""

def max_profit(prices):
    """
    One pass solution - O(n) time, O(1) space
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


if __name__ == "__main__":
    print("Best Time to Buy and Sell Stock Tests:")
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))  # 0
    print(max_profit([2, 4, 1]))  # 2
