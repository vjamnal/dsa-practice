# problem: Maximum Subarray
# approach: Kadane's Algorithm (Dynamic Programming)
# time: O(n)
# space: O(1)

"""
Maximum Subarray
Find the contiguous subarray with the largest sum.
Kadane's Algorithm

LeetCode #53
"""

def max_subarray(nums):
    """
    Kadane's Algorithm - O(n) time, O(1) space
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_with_indices(nums):
    """
    Returns the maximum sum along with start and end indices.
    """
    if not nums:
        return 0, 0, 0
    
    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum = current_sum + nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end


if __name__ == "__main__":
    print("Maximum Subarray Tests:")
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))  # 1
    print(max_subarray([5, 4, -1, 7, 8]))  # 23
