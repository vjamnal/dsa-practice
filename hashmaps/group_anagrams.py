# problem: Group Anagrams
# approach: Hash Map with sorted string as key
# time: O(n * k log k) where n is number of strings, k is max length
# space: O(n * k)

"""
Group Anagrams
Group strings that are anagrams of each other.

LeetCode #49
"""

def group_anagrams(strs):
    """
    Hash map with sorted string as key - O(n * k log k) time
    where n is number of strings, k is max length
    """
    anagram_map = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = []
        anagram_map[sorted_str].append(s)
    
    return list(anagram_map.values())


def group_anagrams_counting(strs):
    """
    Hash map with character count as key - O(n * k) time
    """
    anagram_map = {}
    
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


if __name__ == "__main__":
    print("Group Anagrams Tests:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    print(group_anagrams([""]))  # [[""]]
    print(group_anagrams(["a"]))  # [["a"]]
