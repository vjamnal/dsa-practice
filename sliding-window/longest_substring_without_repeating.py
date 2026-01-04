# problem: Longest Substring Without Repeating Characters
# approach: Sliding Window with Hash Set
# time: O(n)
# space: O(min(n, m)) where m is charset size

"""
Longest Substring Without Repeating Characters
Find the length of the longest substring without repeating characters.

LeetCode #3
"""

def length_of_longest_substring(s):
    """
    Sliding window with hash set - O(n) time, O(min(n, m)) space
    where m is charset size
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


def length_of_longest_substring_optimized(s):
    """
    Optimized sliding window with hash map - O(n) time, O(min(n, m)) space
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    print("Longest Substring Without Repeating Characters Tests:")
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))  # 1
    print(length_of_longest_substring("pwwkew"))  # 3
    print(length_of_longest_substring_optimized("abcabcbb"))  # 3
