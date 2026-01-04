# problem: Valid Anagram
# approach: Hash Map (Frequency Count)
# time: O(n)
# space: O(n)

"""
Valid Anagram
Check if two strings are anagrams of each other.

LeetCode #242
"""

def is_anagram(s, t):
    """
    Sorting approach - O(n log n) time, O(1) space
    """
    return sorted(s) == sorted(t)


def is_anagram_hashmap(s, t):
    """
    Hash map approach - O(n) time, O(n) space
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True


if __name__ == "__main__":
    print("Valid Anagram Tests:")
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))  # False
    print(is_anagram_hashmap("anagram", "nagaram"))  # True
