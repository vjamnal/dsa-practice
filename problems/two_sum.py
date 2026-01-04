"""
Two Sum Problem
Given an array of integers and a target, find two numbers that add up to target.
"""

def two_sum(nums, target):
    """
    Solution 1: Using Hash Map - O(n) time, O(n) space
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_sorted(nums, target):
    """
    Solution 2: Two Pointers (for sorted array) - O(n) time, O(1) space
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# Example usage
if __name__ == "__main__":
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: {nums}, target: {target}")
    print(f"Output: {two_sum(nums, target)}")  # [0, 1]
    
    # Test case 2
    nums = [3, 2, 4]
    target = 6
    print(f"\nInput: {nums}, target: {target}")
    print(f"Output: {two_sum(nums, target)}")  # [1, 2]
