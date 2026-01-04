# problem: Three Sum
# approach: Two Pointers with Sorting
# time: O(n²)
# space: O(1) excluding result

"""
Three Sum
Find all unique triplets that sum to zero.

LeetCode #15
"""

def three_sum(nums):
    """
    Two pointer approach - O(n^2) time, O(1) space (excluding result)
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result


if __name__ == "__main__":
    print("Three Sum Tests:")
    print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))  # []
    print(three_sum([0, 0, 0]))  # [[0, 0, 0]]
