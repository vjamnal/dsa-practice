# problem: Maximum Sum Subarray of Size K
# approach: Fixed-size Sliding Window
# time: O(n)
# space: O(1)

"""
Maximum Sum Subarray of Size K
Find the maximum sum of any contiguous subarray of size k.
"""

def max_sum_subarray(arr, k):
    """
    Fixed-size sliding window - O(n) time, O(1) space
    """
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


if __name__ == "__main__":
    print("Maximum Sum Subarray of Size K Tests:")
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9
    print(max_sum_subarray([2, 3, 4, 1, 5], 2))  # 7
    print(max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # 39
