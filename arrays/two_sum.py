# problem: Two Sum
# approach: Hash Map
# time: O(n)
# space: O(n)

"""
Two Sum Problem
Given an array of integers and a target, find two numbers that add up to target.

LeetCode #1
"""

def two_sum(nums, target):
    """
    Solution using Hash Map - O(n) time, O(n) space
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
    Two Pointers approach (for sorted array) - O(n) time, O(1) space
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


if __name__ == "__main__":
    # Test cases
    print("Two Sum Tests:")
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [0, 1]
