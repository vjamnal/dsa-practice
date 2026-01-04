# problem: Longest Consecutive Sequence
# approach: Hash Set
# time: O(n)
# space: O(n)

"""
Longest Consecutive Sequence
Find the length of the longest consecutive elements sequence.

LeetCode #128
"""

def longest_consecutive(nums):
    """
    Hash set approach - O(n) time, O(n) space
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length


if __name__ == "__main__":
    print("Longest Consecutive Sequence Tests:")
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(longest_consecutive([]))  # 0
