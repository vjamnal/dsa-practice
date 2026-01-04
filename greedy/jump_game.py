# problem: Jump Game
# approach: Greedy (Track max reachable position)
# time: O(n)
# space: O(1)

"""
Jump Game
Determine if you can reach the last index of the array.

LeetCode #55
"""

def can_jump(nums):
    """
    Greedy approach - O(n) time, O(1) space
    Track the furthest reachable position
    """
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    
    return True


def can_jump_backward(nums):
    """
    Backward greedy approach - O(n) time, O(1) space
    """
    goal = len(nums) - 1
    
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return goal == 0


if __name__ == "__main__":
    print("Jump Game Tests:")
    print(can_jump([2, 3, 1, 1, 4]))  # True
    print(can_jump([3, 2, 1, 0, 4]))  # False
    print(can_jump([0]))  # True
    print(can_jump_backward([2, 3, 1, 1, 4]))  # True
