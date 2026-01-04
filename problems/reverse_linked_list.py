"""
Reverse Linked List
Reverse a singly linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list_iterative(head):
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


def reverse_linked_list_recursive(head):
    """
    Recursive solution - O(n) time, O(n) space (call stack)
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_linked_list_recursive(head.next)
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
    print(" -> ".join(values))


# Example usage
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print("Original list:")
    print_list(head)
    
    reversed_head = reverse_linked_list_iterative(head)
    print("\nReversed list:")
    print_list(reversed_head)
