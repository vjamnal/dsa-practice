"""
Searching Algorithms
Various searching algorithm implementations.
"""

def linear_search(arr, target):
    """
    Linear Search - O(n)
    Sequentially checks each element until target is found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search - O(log n)
    Searches a sorted array by repeatedly dividing in half.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary Search (Recursive) - O(log n)
    Recursive implementation of binary search.
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr, target):
    """
    Jump Search - O(√n)
    Works on sorted arrays by jumping ahead by fixed steps.
    """
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1
