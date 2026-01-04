# problem: Longest Common Subsequence
# approach: 2D Dynamic Programming
# time: O(m * n)
# space: O(m * n)

"""
Longest Common Subsequence
Find the length of longest common subsequence between two strings.

LeetCode #1143
"""

def longest_common_subsequence(text1, text2):
    """
    2D Dynamic programming - O(m * n) time, O(m * n) space
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def longest_common_subsequence_optimized(text1, text2):
    """
    Space-optimized DP - O(m * n) time, O(min(m, n)) space
    """
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    
    return prev[n]


if __name__ == "__main__":
    print("Longest Common Subsequence Tests:")
    print(longest_common_subsequence("abcde", "ace"))  # 3
    print(longest_common_subsequence("abc", "abc"))  # 3
    print(longest_common_subsequence("abc", "def"))  # 0
