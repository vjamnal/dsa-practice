# problem: Container With Most Water
# approach: Two Pointers
# time: O(n)
# space: O(1)

"""
Container With Most Water
Find two lines that together with x-axis form a container with most water.

LeetCode #11
"""

def max_area(height):
    """
    Two pointer approach - O(n) time, O(1) space
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


if __name__ == "__main__":
    print("Container With Most Water Tests:")
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))  # 1
    print(max_area([4, 3, 2, 1, 4]))  # 16
