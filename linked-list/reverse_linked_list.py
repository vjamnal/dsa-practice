# problem: Reverse Linked List
# approach: Iterative pointer manipulation
# time: O(n)
# space: O(1)

"""
Reverse Linked List
Reverse a singly linked list.

LeetCode #206
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head):
    """
    Iterative solution - O(n) time, O(1) space
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def reverse_list_recursive(head):
    """
    Recursive solution - O(n) time, O(n) space (call stack)
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


def print_list(head):
    """Helper function to print linked list."""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


if __name__ == "__main__":
    print("Reverse Linked List Tests:")
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Original: {print_list(head)}")
    reversed_head = reverse_list_iterative(head)
    print(f"Reversed: {print_list(reversed_head)}")
