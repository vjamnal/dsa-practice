"""
Maximum Subarray
Find the contiguous subarray with the largest sum.
Kadane's Algorithm
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


# Example usage
if __name__ == "__main__":
    # Test case 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums}")
    print(f"Maximum subarray sum: {max_subarray(nums)}")  # 6
    
    max_sum, start, end = max_subarray_with_indices(nums)
    print(f"Subarray: {nums[start:end+1]}")
    
    # Test case 2
    nums = [1]
    print(f"\nInput: {nums}")
    print(f"Maximum subarray sum: {max_subarray(nums)}")  # 1
    
    # Test case 3
    nums = [5, 4, -1, 7, 8]
    print(f"\nInput: {nums}")
    print(f"Maximum subarray sum: {max_subarray(nums)}")  # 23
