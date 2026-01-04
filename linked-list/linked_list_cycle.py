# problem: Linked List Cycle
# approach: Floyd's Cycle Detection (Two Pointers)
# time: O(n)
# space: O(1)

"""
Linked List Cycle
Detect if a linked list has a cycle.

LeetCode #141
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """
    Floyd's Cycle Detection (Tortoise and Hare) - O(n) time, O(1) space
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True


def has_cycle_hashset(head):
    """
    Hash set approach - O(n) time, O(n) space
    """
    seen = set()
    current = head
    
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    
    return False


if __name__ == "__main__":
    print("Linked List Cycle Tests:")
    # Create cycle: 3 -> 2 -> 0 -> -4 -> (back to 2)
    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle
    
    print(f"Has cycle: {has_cycle(head)}")  # True
    
    # No cycle
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    print(f"Has cycle: {has_cycle(head2)}")  # False
